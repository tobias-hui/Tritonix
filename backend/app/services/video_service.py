
from fastapi import UploadFile
from qiniu import PersistentFop, urlsafe_base64_encode, put_data
from pymongo import MongoClient
from bson import ObjectId

from app.core.config import Config

client = MongoClient(Config.MONGODB_URL)
db = client[Config.MONGO_DB]
collection = db[Config.MONGO_COLLECTION]

class VideoService:
    def __init__(self, qiniu_auth, bucket_name, qiniu_domain):
        self.qiniu_auth = qiniu_auth
        self.bucket_name = bucket_name
        self.qiniu_domain = qiniu_domain


    def get_frame_url(self, video_key: str, cover: bool) -> str:
        pfop = PersistentFop(self.qiniu_auth, self.bucket_name)

        # 裁剪模式2表示等比缩放并且裁剪，可以确保图片不被拉伸
        if cover:
            fops = 'vframe/jpg/offset/1|imageView2/2/w/720/h/1680'
            saveas_key = urlsafe_base64_encode(f'{self.bucket_name}:{video_key}-cover.jpg')
        else:
            fops = 'vframe/jpg/offset/1|imageView2/2/w/360/h/480'
            saveas_key = urlsafe_base64_encode(f'{self.bucket_name}:{video_key}-thumbnail.jpg')

        fops = f'{fops}|saveas/{saveas_key}'

        # 执行pfop操作
        ops = [fops]
        ret, info = pfop.execute(video_key, ops, 1)

        # 检查pfop操作是否成功
        if info.status_code == 200:
            # 生成私有空间的截帧URL
            frame_key = f'{video_key}-cover.jpg' if cover else f'{video_key}-thumbnail.jpg'
            frame_url = self.generate_private_url(frame_key)
            return frame_url
        else:
            raise Exception(f"Failed to pfop for video {video_key}: {info}")


    def generate_private_url(self, key):

        base_url = f'http://{self.qiniu_domain}/{key}'
        private_url = self.qiniu_auth.private_download_url(base_url, expires=3600)
        return private_url
    
    async def upload_to_qiniu(self, file: UploadFile, file_name: str):
        contents = await file.read()  # 读取文件内容
        token = self.qiniu_auth.upload_token(self.bucket_name, file_name)
        ret, info = put_data(token, file_name, contents)  # 使用put_data上传文件内容
        if info.status_code == 200:
            key = ret["key"]  # 文件的key
            return key
        else:
            raise Exception("Upload to qiniu failed")
        
    def get_video_playback_url(self, video_id: str, expires: int = 3600) -> str:
        # 先在默认集合中尝试获取视频
        video = collection.find_one({"_id": ObjectId(video_id)})
        # 如果在默认集合中找不到，尝试在 pet_videos 集合中查找
        if not video:
            pet_collection = db['pet_videos']
            video = pet_collection.find_one({"_id": ObjectId(video_id)})
            if not video:
                raise ValueError("Video not found")

        video_key = video.get("qiniuKey")
        base_url = f'http://{self.qiniu_domain}/{video_key}'
        private_url = self.qiniu_auth.private_download_url(base_url, expires=expires)
        return private_url

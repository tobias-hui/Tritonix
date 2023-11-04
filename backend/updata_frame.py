from pymongo import MongoClient
from qiniu import Auth, PersistentFop, urlsafe_base64_encode

from app.core.config import Config

# 七牛云配置
bucket_name = Config.BUCKET_NAME
qiniu_auth = Auth(Config.ACCESS_KEY, Config.SECRET_KEY)
qiniu_domain = Config.QINIU_DOMAIN

# MongoDB配置
client = MongoClient(Config.MONGODB_URL)
db = client[Config.MONGO_DB]
collection = db[Config.MONGO_COLLECTION]

# 根据七牛云kodo存储的视频截帧功能，将视频截帧保存至数据表
def video_frame_update():
    pfop = PersistentFop(qiniu_auth, bucket_name)

    for video in collection.find({}):
        video_key = video['qiniuKey']
        # 构建截帧操作指令
        fops = f'vframe/jpg/offset/1/w/480/h/360'
        saveas_key = urlsafe_base64_encode(f'{bucket_name}:{video_key}-frame.jpg')
        fops = f'{fops}|saveas/{saveas_key}'

        # 执行pfop操作
        ops = [fops]
        ret, info = pfop.execute(video_key, ops, 1)

        # 检查pfop操作是否成功
        if info.status_code == 200:
            # 生成私有空间的截帧URL
            frame_key = f'{video_key}-frame.jpg'
            frame_url = generate_private_url(qiniu_domain, frame_key)
            print(frame_url)
            # 更新MongoDB记录
            collection.update_one({'_id': video['_id']}, {'$set': {'frame_url': frame_url}})
        else:
            print(f"Failed to pfop for video {video_key}: {info}")

    print("All video frames have been updated.")

def generate_private_url(domain, key):
    # 有效时间：3600秒
    base_url = f'http://{domain}/{key}'
    private_url = qiniu_auth.private_download_url(base_url, expires=3600)
    return private_url

video_frame_update()

# /backend/app/services/video_service.py

from qiniu import PersistentFop, urlsafe_base64_encode

class VideoService:
    def __init__(self, qiniu_auth, bucket_name, qiniu_domain):
        self.qiniu_auth = qiniu_auth
        self.bucket_name = bucket_name
        self.qiniu_domain = qiniu_domain

    def get_frame_url(self, video_key):
        pfop = PersistentFop(self.qiniu_auth, self.bucket_name)

        # 构建截帧操作指令
        fops = f'vframe/jpg/offset/1/w/400/h/360'
        saveas_key = urlsafe_base64_encode(f'{self.bucket_name}:{video_key}-frame.jpg')
        fops = f'{fops}|saveas/{saveas_key}'

        # 执行pfop操作
        ops = [fops]
        ret, info = pfop.execute(video_key, ops, 1)

        # 检查pfop操作是否成功
        if info.status_code == 200:
            # 生成私有空间的截帧URL
            frame_key = f'{video_key}-frame.jpg'
            frame_url = self.generate_private_url(frame_key)
            return frame_url
        else:
            print(f"Failed to pfop for video {video_key}: {info}")

    def generate_private_url(self, key):

        base_url = f'http://{self.qiniu_domain}/{key}'
        private_url = self.qiniu_auth.private_download_url(base_url, expires=3600)
        return private_url

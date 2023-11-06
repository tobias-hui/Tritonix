from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    # 七牛云配置
    ACCESS_KEY = os.getenv("ACCESSKEY")
    SECRET_KEY = os.getenv("SECRETKEY")
    BUCKET_NAME = 'tritonix0'
    QINIU_DOMAIN = 's39r2f5eu.bkt.clouddn.com'

    # MongoDb配置
    MONGODB_URL = os.getenv("MONGODB_URL")
    MONGO_DB = 'videos'
    MONGO_COLLECTION = 'douyin_videos'
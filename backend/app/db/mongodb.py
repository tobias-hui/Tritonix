from pymongo import MongoClient
from qiniu import Auth, urlsafe_base64_encode

from app.core.config import Config
from app.services.video_service import VideoService

# Replace with your actual connection string
client = MongoClient(Config.MONGODB_URL)
db = client[Config.MONGO_DB]
collection = db[Config.MONGO_COLLECTION]

# 初始化VideoService
video_service = VideoService(Auth(Config.ACCESS_KEY, Config.SECRET_KEY ), Config.BUCKET_NAME, Config.QINIU_DOMAIN)

def get_categories():
    categories = collection.distinct("categories")
    categories.append("pet")
    return categories


def get_videos_by_category(category_id, skip, limit):
    if category_id == "pet":
        pet_collection = db['pet_videos']  # 单独的集合
        cursor = pet_collection.find({}).skip(skip).limit(limit)
    else:
        cursor = collection.find({"categories": category_id}).skip(skip).limit(limit)
    videos = list(cursor)  # 将游标转换成列表

    for video in videos:
        video_key = video['qiniuKey']
        video['frame_url'] = video_service.get_frame_url(video_key)
    return videos



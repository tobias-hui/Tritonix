from pymongo import MongoClient
from qiniu import Auth
from bson import ObjectId, errors
from datetime import datetime
from typing import List

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


def get_videos_by_category(category_id: str, skip: int, limit: int):
    if category_id == "pet":
        pet_collection = db['pet_videos']  # 单独的集合
        cursor = pet_collection.find({}).skip(skip).limit(limit)
    else:
        cursor = collection.find({"categories": category_id}).skip(skip).limit(limit)
    videos = list(cursor)  # 将游标转换成列表

    for video in videos:
        video_key = video['qiniuKey']
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
    return videos

def get_video_detail(video_id: str):
    video = collection.find_one({"_id": ObjectId(video_id)})
    if not video:
        pet_collection = db['pet_videos']
        video = pet_collection.find_one({"_id": ObjectId(video_id)})
    if video:
        video_key = video['qiniuKey']
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
        return video
    return None

def insert_video_data(video_key: str, video_categories: str, video_descroption: str):
    video_document = {
        "create_time": datetime.now().isoformat(),
        "favoriting_count": 0,
        "follower_count": 0,
        "description": video_descroption,
        "collect_count": 0,
        "comment_count": 0,
        "digg_count": 0,
        "share_count": 0,
        "qiniuKey": video_key,
        "uploadedAt": datetime.now(),
        "categories": video_categories,        
    }
    result = collection.insert_one(video_document)
    video_id = result.inserted_id
    # 更新文档，添加id字段
    collection.update_one(
        {'_id': video_id},
        {'$set': {'id': str(video_id)}}
    )
    return str(video_id)

def search_videos(keyword: str) -> List[dict]:
    """Search for videos based on a keyword."""
    query = {"description": {"$regex": keyword, "$options": "i"}}  # Case-insensitive search
    results = collection.find(query)
    videos = list(results)

    for video in videos:
        video_key = video['qiniuKey']
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
    return videos

def get_mixed_videos(skip: int, limit: int):
    # 使用聚合管道随机获取视频
    pipeline = [
        {"$sample": {"size": limit}},  # 随机获取指定数量的视频
        {"$skip": skip}  # 跳过前面的视频，实现分页
    ]
    videos = list(collection.aggregate(pipeline))
    for video in videos:
        video_key = video['qiniuKey']
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
    return videos



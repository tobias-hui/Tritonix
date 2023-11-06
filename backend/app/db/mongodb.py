from pymongo import MongoClient
from qiniu import Auth
from bson import ObjectId, errors
from datetime import datetime
from typing import List
from werkzeug.security import generate_password_hash

from app.core.config import Config
from app.services.video_service import VideoService
from app.schemas.user import UserCreate, UserInDB

# Replace with your actual connection string
client = MongoClient(Config.MONGODB_URL)
db = client[Config.MONGO_DB]
collection = db[Config.MONGO_COLLECTION]
users_db = client[Config.MONGO_USER_DB]
users_collection = users_db[Config.MONGO_USER_COLLECTION]

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
        base_url = f'http://{video_service.qiniu_domain}/{video_key}'
        private_url = video_service.qiniu_auth.private_download_url(base_url, expires=3600)
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
        print(private_url)
        video['playback_url'] = private_url

    return videos

def get_video_detail(video_id: str):
    video = collection.find_one({"_id": ObjectId(video_id)})
    if not video:
        pet_collection = db['pet_videos']
        video = pet_collection.find_one({"_id": ObjectId(video_id)})
    if video:
        video_key = video['qiniuKey']
        base_url = f'http://{video_service.qiniu_domain}/{video_key}'
        private_url = video_service.qiniu_auth.private_download_url(base_url, expires=3600)
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
        video['playback_url'] = private_url
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
        base_url = f'http://{video_service.qiniu_domain}/{video_key}'
        private_url = video_service.qiniu_auth.private_download_url(base_url, expires=3600)
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
        video['playback_url'] = private_url
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
        base_url = f'http://{video_service.qiniu_domain}/{video_key}'
        private_url = video_service.qiniu_auth.private_download_url(base_url, expires=3600)
        video['frame_url'] = video_service.get_frame_url(video_key, False)
        video['cover_url'] = video_service.get_frame_url(video_key, True)
        video['playback_url'] = private_url
    return videos


def create_user(user_in: UserCreate) -> UserInDB:
    hashed_password = generate_password_hash(user_in.password)
    user_data = user_in.model_dump()
    user_data['hashed_password'] = hashed_password
    user_data['created_at'] = datetime.utcnow()
    result = users_collection.insert_one(user_data)
    # 更新文档，添加id字段
    user_data["id"] = str(result.inserted_id)
    users_collection.update_one(
        {'_id': result.inserted_id},
        {'$set': {'id': str(result.inserted_id)}}
    )
    return UserInDB(**user_data)

def get_user_by_email(email: str) -> UserInDB:
    user_data = users_collection.find_one({"email": email})
    return UserInDB(**user_data) if user_data else None

def add_video_to_likes(user_id: str, video_id: str):
    users_collection.update_one(
        {"id": user_id},
        {"$addToSet": {"like": video_id}}  # $addToSet 防止重复添加
    )
    print(users_collection.find_one({"_id": user_id}))

def remove_video_from_likes(user_id: str, video_id: str):
    users_collection.update_one(
        {"id": user_id},
        {"$pull": {"like": video_id}}  # $pull 用来移除数组中的元素
    )

def add_user_to_follow(user_id: str, follow_user_id: str):
    users_collection.update_one(
        {"id": user_id},
        {"$addToSet": {"follow": follow_user_id}}
    )

def remove_user_from_following(user_id: str, video_id: str):
    users_collection.update_one(
        {"id": user_id},
        {"$pull": {"follow": video_id}}  # $pull 用来移除数组中的元素
    )

def add_video_to_collect(user_id: str, video_id: str):
    users_collection.update_one(
        {"id": user_id},
        {"$addToSet": {"collection": video_id}}  # $addToSet 防止重复添加
    )

def remove_video_from_collected(user_id: str, video_id: str):
    users_collection.update_one(
        {"id": user_id},
        {"$pull": {"collection": video_id}}  # $pull 用来移除数组中的元素
    )

def get_user_likes(user_id: str) -> List[str]:
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    return user_data["like"] if user_data and "like" in user_data else []

def get_user_following(user_id: str) -> List[str]:
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    return user_data["follow"] if user_data and "like" in user_data else []

def get_user_collection(user_id: str) -> List[str]:
    user_data = users_collection.find_one({"_id": ObjectId(user_id)})
    return user_data["collection"] if user_data and "like" in user_data else []
from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from typing import List
from qiniu import Auth

from app.db.mongodb import get_categories, get_videos_by_category, get_video_detail, insert_video_data, search_videos
from app.schemas.video import Category, Video
from app.services.video_service import VideoService
from app.core.config import Config

router = APIRouter()

# 初始化VideoService
video_service = VideoService(Auth(Config.ACCESS_KEY, Config.SECRET_KEY ), Config.BUCKET_NAME, Config.QINIU_DOMAIN)

@router.get("/categories", response_model=List[Category])
async def read_categories():
    categories = get_categories()
    return [{"name": category} for category in categories]

@router.get("/categories/{category_id}/videos", response_model=List[Video])
async def read_videos_by_category(category_id: str, skip: int = 0, limit: int = 10):
    videos = get_videos_by_category(category_id, skip, limit)
    if videos is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return videos

@router.get("/videos/search", response_model=List[Video])
async def api_search_videos(keyword: str = Query(..., description="Search videos by keyword")):
    """Search videos by keyword."""
    videos = search_videos(keyword)
    return videos

@router.get("/videos/{video_id}", response_model=Video)
async def read_video_detail(video_id: str):
    video = get_video_detail(video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@router.post("/videos", response_model=Video)
async def insert_video(name: str, description: str, categories: str, file: UploadFile = File(...)):
    # 使用Service上传文件到七牛云
    video_key = await video_service.upload_to_qiniu(file, name)
    # 将视频数据插入数据库
    video_id = insert_video_data(video_key, categories, description)
    video = get_video_detail(video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video


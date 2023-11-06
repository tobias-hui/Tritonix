from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from typing import List
from qiniu import Auth

from app.db.mongodb import get_categories, get_videos_by_category, get_video_detail, insert_video_data, search_videos, get_mixed_videos
from app.schemas.video import Category, Video
from app.services.video_service import VideoService
from app.core.config import Config

router = APIRouter()

# 初始化VideoService
video_service = VideoService(Auth(Config.ACCESS_KEY, Config.SECRET_KEY ), Config.BUCKET_NAME, Config.QINIU_DOMAIN)

@router.get("/categories", response_model=List[Category], name='获取所有的视频类别', tags=["视频信息"], description="获取数据库当中所有的视频类别")
async def read_categories():
    categories = get_categories()
    return [{"name": category} for category in categories]

@router.get("/categories/{category_id}/videos", response_model=List[Video],  tags=["视频信息"], name="获取某个视频类别下的所有视频",description="获取某个视频类别下的所有视频的信息")
async def read_videos_by_category(category_id: str, skip: int = 0, limit: int = 10):
    videos = get_videos_by_category(category_id, skip, limit)
    if videos is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return videos

@router.get("/videos/search", response_model=List[Video], tags=["视频信息"], name="搜索视频", description="根据关键字搜索视频")
async def api_search_videos(keyword: str = Query(..., description="Search videos by keyword")):
    """Search videos by keyword."""
    videos = search_videos(keyword)
    return videos

@router.get("/videos/recommend", response_model=List[Video], tags=["视频信息"], name="推荐视频", description="获取进入app后的推荐视频")
async def recommended_videos(skip: int = Query(0, description="Number of records to skip"), limit: int = Query(10, description="Size of each page")):
    videos = get_mixed_videos(skip, limit)
    if videos is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return videos

@router.get("/videos/{video_id}", response_model=Video, tags=["视频信息"], name="获取视频详情", description="获取某个视频的详细信息")
async def read_video_detail(video_id: str):
    video = get_video_detail(video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@router.post("/videos", response_model=Video, description="用户自行上传一个视频并获取视频信息", tags=["上传视频"], name="上传视频")
async def insert_video(name: str, description: str, categories: str, file: UploadFile = File(...)):
    # 使用Service上传文件到七牛云
    video_key = await video_service.upload_to_qiniu(file, name)
    # 将视频数据插入数据库
    video_id = insert_video_data(video_key, categories, description)
    video = get_video_detail(video_id)
    if video is None:
        raise HTTPException(status_code=404, detail="Video not found")
    return video

@router.get("/videos/{video_id}/playback-url", tags=["视频播放"], name="获取视频播放地址", description="获取某个视频的播放地址", deprecated=True)
async def get_video_playback_url(video_id: str):
    try:
        playback_url = video_service.get_video_playback_url(video_id)
        return {"playback_url": playback_url}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/videos/{video_id}/share-link", tags=["视频分享"], name="生成视频分享链接", description="为视频生成可分享的链接")
async def generate_share_link(video_id: str):
    try:
        playback_url = video_service.get_video_playback_url(video_id)
        return {"share_link": playback_url}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))

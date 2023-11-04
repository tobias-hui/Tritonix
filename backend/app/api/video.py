from fastapi import APIRouter
from typing import List
from app.db.mongodb import get_categories, get_videos_by_category
from app.schemas.video import Category, Video

router = APIRouter()


@router.get("/categories", response_model=List[Category])
async def read_categories():
    categories = get_categories()
    return [{"name": category} for category in categories]

@router.get("/categories/{category_id}/videos", response_model=List[Video])
async def read_videos_by_category(category_id: str, skip: int = 0, limit: int = 10):
    videos = get_videos_by_category(category_id, skip, limit)
    return videos

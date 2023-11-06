from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from fastapi import UploadFile, File


    
class Video(BaseModel):
    id: Optional[str] = Field(None)
    create_time: str
    favoriting_count: int
    follower_count: int
    description: str
    collect_count: int
    comment_count: int
    digg_count: int
    share_count: int
    qiniuKey: str
    uploadedAt: datetime
    categories: Optional[str] = Field(None)
    game: Optional[str] = Field(None)
    frame_url: Optional[str] = Field(None)
    cover_url: Optional[str] = Field(None)
    playback_url: Optional[str] = Field(None)

class Category(BaseModel):
    name: str


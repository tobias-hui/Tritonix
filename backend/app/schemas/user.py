from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime




class UserBase(BaseModel):
    email: EmailStr  # 使用Pydantic的EmailStr来验证电子邮箱格式
    username: str = Field(..., min_length=3, max_length=50)
    avatar: Optional[str] = Field("https://ibb.co/NrhsTc5", description="URL of the user's avatar")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserInDB(UserBase):
    id: Optional[str] = Field(None, description="Unique identifier in the database")
    hashed_password: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    collection: List[str] = []  # 用户收藏的视频ID列表
    like: List[str] = []  # 用户点赞的视频ID列表
    follow: List[str] = []  # 用户关注的用户ID列表

class UserPublic(UserBase):
    id: str  # 用户的唯一标识符
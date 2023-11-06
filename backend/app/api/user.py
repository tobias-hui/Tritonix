from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from pydantic import ValidationError
from jose import jwt

from app.schemas.user import UserCreate, UserPublic, UserInDB
from app.services.user_service import UserService
from app.db.mongodb import add_user_to_follow, add_video_to_likes, add_video_to_collect, get_user_by_email, get_user_likes, get_user_following, get_user_collection, remove_video_from_likes, remove_user_from_following, remove_video_from_collected
from app.core.config import Config

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/users/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, Config.SECRET, algorithms=[Config.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        # 从数据库获取用户的函数
        user = get_user_by_email(email)
        if user is None:
            raise credentials_exception
    except jwt.JWTError:
        raise credentials_exception
    except ValidationError:
        raise credentials_exception
    return user

@router.post("/users/register", response_model=UserPublic, tags=["用户"], name="注册一个新用户", description="注册一个新用户并将用户信息保存至数据库")
async def register_user(user_in: UserCreate):
    user = UserService.register_new_user(user_in)
    return user

@router.post("/users/login", tags=["用户"], name="用户登录", description="用户登录并返回JWT令牌")
async def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    user = UserService.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token_expires = timedelta(minutes=Config.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = UserService.create_access_token(
        data={"sub": user.email},  # 使用email作为JWT的subject
        expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.put("/users/{user_id}/like/{video_id}", tags=["用户互动"], name="用户点赞视频", description="用户点赞视频")
async def like_video(user_id: str, video_id: str, current_user=Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    add_video_to_likes(user_id, video_id)
    return {"message": "Video added to likes"}

@router.get("/users/me", response_model=UserPublic, tags=["用户"], name="获取当前用户信息", description="获取已验证用户的公共信息")
async def get_current_user_info(current_user: UserInDB = Depends(get_current_user)):
    return current_user

@router.put("/users/{user_id}/follow/{follow_user_id}", tags=["用户互动"], name="用户关注另一个用户", description="用户关注另一个用户")
async def follow_user(user_id: str, follow_user_id: str, current_user=Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    add_user_to_follow(user_id, follow_user_id)
    return {"message": "User followed"}

@router.put("/users/{user_id}/collect/{video_id}", tags=["用户互动"], name="用户收藏视频", description="用户收藏视频")
async def collect_video(user_id: str, video_id: str, current_user=Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    add_video_to_collect(user_id, video_id)
    return {"message": "Video added to collection"}

@router.get("/users/{user_id}/like", tags=["用户互动"], name="获取用户点赞的视频", description="获取用户点赞的视频")
async def get_user_likes_route(user_id: str, current_user: UserInDB = Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    liked_videos = get_user_likes(current_user.id)
    return liked_videos

@router.get("/users/{user_id}/follow", tags=["用户互动"], name="获取用户关注的用户", description="获取用户关注的用户")
async def get_user_following(user_id: str, current_user: UserInDB = Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    followed_users = get_user_following(current_user.id)
    return followed_users

@router.get("/users/{user_id}/collect", tags=["用户互动"], name="获取用户收藏的视频", description="获取用户收藏的视频")
async def get_user_collection(user_id: str, current_user: UserInDB = Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    collected_videos = get_user_collection(current_user.id)
    return collected_videos

@router.delete("/users/{user_id}/like/{video_id}", tags=["用户互动"], name="用户取消点赞视频", description="用户取消点赞视频")
async def unlike_video(user_id: str, video_id: str, current_user=Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    remove_video_from_likes(user_id, video_id)
    return {"message": "Video removed from likes"}

@router.delete("/users/{user_id}/follow/{follow_user_id}", tags=["用户互动"], name="用户取消关注另一个用户", description="用户取消关注另一个用户")
async def unfollow_user(user_id: str, follow_user_id: str, current_user=Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    remove_user_from_following(user_id, follow_user_id)
    return {"message": "User unfollowed"}

@router.delete("/users/{user_id}/collect/{video_id}", tags=["用户互动"], name="用户取消收藏视频", description="用户取消收藏视频")
async def uncollect_video(user_id: str, video_id: str, current_user=Depends(get_current_user)):
    if user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to perform this action")
    remove_video_from_collected(user_id, video_id)
    return {"message": "Video removed from collection"}
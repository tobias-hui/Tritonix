from werkzeug.security import check_password_hash
import jwt
from datetime import datetime, timedelta

from app.db.mongodb import create_user, get_user_by_email
from app.schemas.user import UserCreate, UserInDB
from app.core.config import Config

class UserService:
    @staticmethod
    def register_new_user(user_in: UserCreate) -> UserInDB:
        # 验证邮箱是否已被注册
        existing_user = get_user_by_email(user_in.email)
        if existing_user:
            raise Exception("Email already registered")
        # 创建新用户
        user_in_db = create_user(user_in)
        return user_in_db

    @staticmethod
    def authenticate_user(email: str, password: str) -> UserInDB:
        # 实现用户验证逻辑
        user = get_user_by_email(email)
        if not user or not check_password_hash(user.hashed_password, password):
            raise Exception("Incorrect email or password")
        return user
    
    @staticmethod
    def create_access_token(data: dict, expires_delta: timedelta = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)  # 默认15分钟后过期
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, Config.SECRET, algorithm=Config.ALGORITHM)
        return encoded_jwt
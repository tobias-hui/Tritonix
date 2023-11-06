from fastapi import HTTPException, FastAPI

from app.api.video import router as video_router
from app.api.user import router as user_router

app = FastAPI()

app.include_router(video_router, prefix="/api/v1")

app.include_router(user_router, prefix="/api/v1")

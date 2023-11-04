from fastapi import HTTPException, FastAPI
from app.api.video import router as video_router

app = FastAPI()

app.include_router(video_router, prefix="/api/v1")



from fastapi import HTTPException, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.video import router as video_router
from app.api.user import router as user_router

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(video_router, prefix="/api/v1")

app.include_router(user_router, prefix="/api/v1")

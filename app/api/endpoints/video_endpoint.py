from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.contracts.request.create_video_request import VideoCreateRequest
from app.api.contracts.request.update_video_request import VideoUpdateRequest
from app.api.contracts.response.create_video_response import VideoCreateResponse
from app.api.contracts.response.delete_video_response import VideoDeleteResponse
from app.api.contracts.response.get_video_response import VideoGetResponse
from app.api.contracts.response.update_video_response import VideoUpdateResponse
from app.helpers.database_helper import get_db
from app.models.dto.VideoDTO import VideoDTO
from app.services.video_service import VideoService

# Crear un router para los endpoints relacionados con "videos"
router = APIRouter()

# Dependencia para inyectar el servicio de Libro
def get_video_service(db: Session = Depends(get_db)):
    return VideoService(db)

@router.post("/videos/", response_model=VideoCreateResponse)
def create_video(video_request: VideoCreateRequest, video_service: VideoService = Depends(get_video_service)):
    request_dto = VideoDTO(**video_request.model_dump())
    video_dto = video_service.create_video(request_dto)
    return VideoCreateResponse(**video_dto.dict())

@router.get("/videos/{video_id}", response_model=VideoGetResponse)
def get_video(video_id: int, video_service: VideoService = Depends(get_video_service)):
    video_dto = video_service.get_video(video_id)
    return VideoGetResponse(**video_dto.dict())

@router.get("/videos/", response_model=list[VideoGetResponse])
def get_videos(skip: int = 0, limit: int = 10, video_service: VideoService = Depends(get_video_service)):
    videos_dto = video_service.get_videos(skip, limit)
    return [VideoGetResponse(**video.dict()) for video in videos_dto]

@router.put("/videos/{video_id}", response_model=VideoUpdateResponse)
def update_video(video_id: int, video_request: VideoUpdateRequest, video_service: VideoService = Depends(get_video_service)):
    request_dto = VideoDTO(**video_request.model_dump())
    video_dto = video_service.update_video(video_id, request_dto)
    return VideoUpdateResponse(**video_dto.dict())

@router.delete("/videos/{video_id}", response_model=VideoDeleteResponse)
def delete_video(video_id: int, video_service: VideoService = Depends(get_video_service)):
    video_dto = video_service.delete_video(video_id)
    return VideoDeleteResponse(**video_dto.dict())
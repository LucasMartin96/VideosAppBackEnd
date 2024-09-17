


from sqlalchemy.orm import Session
from fastapi import HTTPException

from app.data.video_dao import VideoDAO
from app.models.dto.VideoDTO import VideoDTO


# Service class: Here goes the logic, validations etc. A class that ensures layers separation for mid-
# complexity app

class VideoService:
    def __init__(self, db: Session):
        self.dao = VideoDAO(db)

    def get_video(self, video_id: int) -> VideoDTO:
        video = self.dao.get_video(video_id)
        if not video:
            raise HTTPException(status_code=404, detail="Video not found")
        return video

    def get_videos(self, skip: int = 0, limit: int = 10) -> list[VideoDTO]:
        return self.dao.get_videos(skip, limit)

    def create_video(self, video_dto: VideoDTO) -> VideoDTO:
        # BL validation example
        # We could do it with a domain layer if necessary, it will make it easier to maintain and read

        if video_dto.duration <= 0:
            raise HTTPException(status_code=400, detail="Duration must be greather than 0")
        if len(video_dto.name) < 3:
            raise HTTPException(status_code=400, detail="Name must have more than 3 characters")

        return self.dao.create_video(video_dto)

    def update_video(self, video_id: int, video_dto: VideoDTO) -> VideoDTO:
        video_to_edit = self.dao.get_video(video_id)

        if not video_to_edit:
            raise HTTPException(status_code=404, detail="Video not found")

        return self.dao.update_video(video_id, video_dto)

    def delete_video(self, video_id: int) -> VideoDTO:
        video_to_delete = self.dao.get_video(video_id)

        if not video_to_delete:
            raise HTTPException(status_code=404, detail="Video not found")

        return self.dao.delete_video(video_id)
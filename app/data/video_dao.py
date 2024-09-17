from sqlalchemy.orm import Session

from app.models.data.video_model import Video
from app.models.dto.VideoDTO import VideoDTO


## It's easier to implement multiple CRUDs if we implement a base class for it, that will contain all the crud logic
## with the database

class VideoDAO:
    def __init__(self, db: Session):
        self.db = db

    def get_video(self, video_id: int) -> VideoDTO:
        result = self.db.query(Video).filter(Video.id == video_id).first()
        return VideoDTO(**result.__dict__)

    def get_videos(self, skip: int = 0, limit: int = 10) -> list[VideoDTO]:
        result = self.db.query(Video).offset(skip).limit(limit).all()
        return [VideoDTO(**video.__dict__) for video in result]

    def create_video(self, video: VideoDTO) -> VideoDTO:
        db_video = Video(**video.dict())
        self.db.add(db_video)
        self.db.commit()
        self.db.refresh(db_video)
        return VideoDTO(**db_video.__dict__)

    def update_video(self, video_id: int, video: VideoDTO) -> VideoDTO:
        db_video = self.db.query(Video).filter(Video.id == video_id).first()
        if db_video:
            for key, value in video.__dict__.items():
                if key != 'id':
                    setattr(db_video, key, value)
            self.db.commit()
            self.db.refresh(db_video)
        return VideoDTO(**db_video.__dict__)

    def delete_video(self, video_id: int) -> VideoDTO:
        db_video = self.db.query(Video).filter(Video.id == video_id).first()
        if db_video:
            self.db.delete(db_video)
            self.db.commit()
        return VideoDTO(**db_video.__dict__)
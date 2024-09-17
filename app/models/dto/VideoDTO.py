from pydantic import BaseModel

class VideoDTO(BaseModel):
    id: int | None = None
    name: str
    author: str
    duration: int
    src: str
    topic: str
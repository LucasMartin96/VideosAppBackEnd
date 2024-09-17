from pydantic import BaseModel

class VideoBaseContract(BaseModel):
    name: str
    author: str
    duration: int
    src: str
    topic: str

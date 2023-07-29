from pydantic import BaseModel


class MediaModelOut(BaseModel):
    id: int
    link: str


class MessageDeliveredModelIn(BaseModel):
    id: int

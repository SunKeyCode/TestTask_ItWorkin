import datetime

from pydantic import BaseModel, Field


class MessageBaseModel(BaseModel):
    sender: int
    recipient: int
    text: str


class MessageSendModelIn(MessageBaseModel):
    pass


class MessageSendModelOut(MessageBaseModel):
    id: int

    sender: int = Field(alias="sender_id")
    recipient: int = Field(alias="recipient_id")
    created_at: datetime.datetime

    class Config:
        from_attributes = True
        populate_by_name = True

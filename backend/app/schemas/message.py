import datetime

from pydantic import BaseModel, Field


class MessageBaseModel(BaseModel):
    recipient: int
    text: str


class MessageSendModelIn(MessageBaseModel):
    pass


class MessageSendModelOut(MessageBaseModel):
    id: int

    sender: int = Field(alias="sender_id")
    recipient: int = Field(alias="recipient_id")
    created_at: datetime.datetime
    is_delivered: bool

    class Config:
        from_attributes = True
        populate_by_name = True

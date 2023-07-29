from datetime import datetime

from sqlalchemy import Integer, Identity, ForeignKey, Text, DateTime, Boolean
from sqlalchemy.orm import mapped_column, Mapped

from db_alchemy.base_class import Base


class Message(Base):
    __tablename__ = "message"

    id = mapped_column(Integer, Identity(always=True), primary_key=True)
    sender_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    recipient_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    text = mapped_column(Text, nullable=False)
    created_at = mapped_column(DateTime, default=datetime.now)
    is_delivered: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

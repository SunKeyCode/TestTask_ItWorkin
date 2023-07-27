from typing import Sequence

from sqlalchemy import select

from crud.base_class import BaseDBRepo
from models.message import Message


class MessageDBRepo(BaseDBRepo):

    async def create(self, sender, recipient, text: str) -> Message:
        async with self.session.begin():
            message = Message(sender_id=sender, recipient_id=recipient, text=text)
            self.session.add(message)

        return message

    async def get_undelivered(
            self, recipient, limit=100, offset=0,
    ) -> Sequence[Message]:
        messages = await self.session.scalars(
            select(Message)
            .where(Message.recipient_id == recipient)
            .limit(limit)
            .offset(offset)
        )

        return messages.all()

    async def set_message_as_delivered(self, message_id: int) -> None:
        pass

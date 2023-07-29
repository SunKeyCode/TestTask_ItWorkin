from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from crud.base_class import BaseDBRepo
from models.message import Message
from models.user import User


class MessageDBRepo(BaseDBRepo):
    def __init__(self, session: AsyncSession, user: User):
        super().__init__(session=session)
        self.current_user = user

    async def create(self, recipient, text: str) -> Message:
        async with self.session.begin():
            message = Message(
                sender_id=self.current_user.id,
                recipient_id=recipient,
                text=text,
            )
            self.session.add(message)

        return message

    async def get_undelivered(
        self,
        limit=100,
        offset=0,
    ) -> Sequence[Message]:
        messages = await self.session.scalars(
            select(Message)
            .where(
                Message.recipient_id == self.current_user.id,
                Message.is_delivered == False,
            )
            .limit(limit)
            .offset(offset)
        )

        return messages.all()

    async def set_message_as_delivered(self, id: int) -> None:
        async with self.session.begin():
            message = await self.session.get(Message, id)
            message.is_delivered = True

        return message

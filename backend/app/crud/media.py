from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from crud.base_class import BaseDBRepo
from models.image import Image
from models.user import User, UserProfile


class MediaDBRepo(BaseDBRepo):

    def __init__(self, session: AsyncSession, user: User):
        super().__init__(session=session)
        self.current_user = user

    async def create_avatar(self, link: str):
        async with self.session.begin():
            avatar = Image(link=link)
            profile = await self.session.scalar(
                select(UserProfile).where(UserProfile.user_id == self.current_user.id)
                .options(joinedload(UserProfile.avatar))
            )
            self.session.add(avatar)
            profile.avatar = avatar

        return avatar

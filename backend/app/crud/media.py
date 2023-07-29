from models.image import Image


async def create_ava(session, user_id, link: str):
    async with session.begin():
        avatar = Image(link=link)
        session.add(avatar)

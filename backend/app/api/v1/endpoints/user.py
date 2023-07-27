from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from dependencies.db_session import get_db_session
from schemas.message import MessageSendModelIn, MessageSendModelOut
from crud.user import UserBDSearchManager

router = APIRouter(prefix="/users")


@router.get("/search")
async def search_users(
        fragment: str,
        session: AsyncSession = Depends(get_db_session),
):
    users = await UserBDSearchManager(session).search_user(
        fragment=fragment
    )
    return users

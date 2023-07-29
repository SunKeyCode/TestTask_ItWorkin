from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from dependencies.db_session import get_db_session
from crud.user import UserBDSearchRepo

from schemas.user import UserReadSchema

router = APIRouter(prefix="/users")


@router.get(
    "/search",
    response_model=list[UserReadSchema],
)
async def search_users(
    fragment: str,
    session: AsyncSession = Depends(get_db_session),
):
    users = await UserBDSearchRepo(session).search_user(fragment=fragment)
    return users

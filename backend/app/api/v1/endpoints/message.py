from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from dependencies.db_session import get_db_session
from dependencies.current_user import get_current_user
from models.user import User
from schemas.media import MessageDeliveredModelIn
from schemas.message import MessageSendModelIn, MessageSendModelOut
from crud.message import MessageDBRepo

router = APIRouter(prefix="/messages")


@router.post(
    "/send",
    description="Creates message",
    response_model=MessageSendModelOut,
    status_code=status.HTTP_201_CREATED,
    response_model_by_alias=False,
)
async def create_message(
    message_data: MessageSendModelIn,
    session: AsyncSession = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
):
    message = await MessageDBRepo(session, current_user).create(
        **message_data.model_dump()
    )

    return message


@router.get(
    "/get_undelivered",
    response_model=list[MessageSendModelOut],
    response_model_by_alias=False,
)
async def get_messages(
    session: AsyncSession = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
):
    messages = await MessageDBRepo(session, current_user).get_undelivered()
    return messages


@router.patch(
    "/delivered",
    status_code=status.HTTP_202_ACCEPTED,
    response_model=MessageSendModelOut,
)
async def set_as_delivered(
    message_data: MessageDeliveredModelIn,
    session: AsyncSession = Depends(get_db_session),
    current_user: User = Depends(get_current_user),
):
    message = await MessageDBRepo(
        session,
        current_user,
    ).set_message_as_delivered(**message_data.model_dump())
    return message

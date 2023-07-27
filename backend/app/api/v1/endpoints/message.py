from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from dependencies.db_session import get_db_session
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
):
    message = await MessageDBRepo(session).create(**message_data.model_dump())

    return message


@router.get(
    "/get",
    response_model=list[MessageSendModelOut],
    response_model_by_alias=False,
)
async def get_messages(
        session: AsyncSession = Depends(get_db_session),
):
    messages = await MessageDBRepo(session).get_undelivered(3)
    return messages


# @router.patch(
#     "/delivered",
#     status_code=status.HTTP_204_NO_CONTENT,
# )
# async def set_as_delivered(
#         message_data: "MessageDeliveredModelIn",
#         session: AsyncSession = Depends(get_db_session),
# ):
#     message = await MessageDBManager.set_message_as_delivered(
#         **message_data.model_dump()
#     )
#     return message

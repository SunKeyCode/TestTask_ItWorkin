from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from dependencies.current_user import get_current_user
from dependencies.db_session import get_db_session
from core.upload_file import upload_file
from crud.media import create_ava
from models.user import User

router = APIRouter(prefix="/media")


@router.post(
    "/avatar/create",
    status_code=status.HTTP_201_CREATED,
    # response_model=MediaModelOut,
)
async def create_avatar(
        file: UploadFile,
        session: AsyncSession = Depends(get_db_session),
        # current_user: User = Depends(get_current_user),
) -> dict[str, int]:
    link = await upload_file(file)
    await create_ava(session, 1, link)
    return {"res": True}

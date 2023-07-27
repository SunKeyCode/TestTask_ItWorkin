from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Integer, Identity, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship, Mapped

from db_alchemy.base_class import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    id = mapped_column(Integer, Identity(always=True), primary_key=True)
    username = mapped_column(String, nullable=False, unique=True)

    profile: Mapped["UserProfile"] = relationship(back_populates="user")


class UserProfile(Base):
    __tablename__ = "table_profile"

    id = mapped_column(Integer, Identity(always=True), primary_key=True)
    phone = mapped_column(String, nullable=True)
    avatar = mapped_column(String, nullable=True)
    user_id = mapped_column(ForeignKey("user.id"))

    user: Mapped[User] = relationship(back_populates="profile")

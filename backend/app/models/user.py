from sqlalchemy import Integer, Identity, String, ForeignKey, Boolean
from sqlalchemy.orm import mapped_column, relationship, Mapped

from models.image import Image
from db_alchemy.base_class import Base


class User(Base):
    __tablename__ = "user"

    id = mapped_column(Integer, Identity(always=True), primary_key=True)
    username: Mapped[int] = mapped_column(String, nullable=False, unique=True)
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    profile: Mapped["UserProfile"] = relationship(back_populates="user", lazy="raise")


class UserProfile(Base):
    __tablename__ = "profile"

    id = mapped_column(Integer, Identity(always=True), primary_key=True)
    phone = mapped_column(String, nullable=True)
    # avatar = mapped_column(String, nullable=True)
    image_id = mapped_column(ForeignKey("image.id"), nullable=True)
    user_id = mapped_column(ForeignKey("user.id"))

    avatar: Mapped["Image"] = relationship(lazy="raise")

    user: Mapped[User] = relationship(back_populates="profile")

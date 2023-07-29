from sqlalchemy import String, Integer, Identity
from sqlalchemy.orm import mapped_column, Mapped

from db_alchemy.base_class import Base


class Image(Base):
    __tablename__ = "image"

    id = mapped_column(Integer, Identity(always=True), primary_key=True)
    link: Mapped[str] = mapped_column(String, nullable=True)

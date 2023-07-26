from sqlalchemy import Integer, Identity, String
from sqlalchemy.orm import mapped_column

from db_alchemy.base_class import Base


class Item(Base):
    __tablename__ = "table_item"

    id = mapped_column(Integer, Identity(always=True), primary_key=True)
    name = mapped_column(String(50), nullable=False)

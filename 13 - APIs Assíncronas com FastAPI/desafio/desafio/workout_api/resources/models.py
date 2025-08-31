from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import UUID
from sqlalchemy.dialects.postgresql import UUID as PG_UUId
from uuid import uuid4
from sqlalchemy.orm import Mapped, mapped_column


class BasicModels(DeclarativeBase):
    id: Mapped[UUID] = mapped_column(PG_UUId(as_uuid=True), primary_key=True, default=uuid4, nullable=False)
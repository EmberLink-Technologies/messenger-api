import uuid
from datetime import date

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.types import String, Date
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import func


class Base(DeclarativeBase): ...


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )
    email: Mapped[str] = mapped_column(
        String(255), unique=True, index=True, nullable=False
    )
    full_name: Mapped[str] = mapped_column(String(255), nullable=False)
    username: Mapped[str] = mapped_column(
        String(255), nullable=False, unique=True, index=True
    )
    phone: Mapped[str | None] = mapped_column(
        String(20), nullable=True, unique=True, index=True
    )
    birthday: Mapped[date | None] = mapped_column(Date, nullable=True)
    registration_at: Mapped[date] = mapped_column(
        Date, server_default=func.current_date(), nullable=False
    )
    password: Mapped[str] = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} with email: {self.email}"

from datetime import datetime, timezone
from decimal import Decimal
from typing import List

from sqlalchemy import (
    DateTime,
    Enum,
    Integer,
    Numeric,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base
from app.models.enums import PaymentMethod


class Sale(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(primary_key=True)

    customer_id: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True,
    )

    payment_method: Mapped[PaymentMethod] = mapped_column(
        Enum(PaymentMethod),
        nullable=False,
    )

    total_amount: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    sale_items: Mapped[List["SaleItem"]] = relationship(
        back_populates="sale",
        cascade="all, delete-orphan",
    )
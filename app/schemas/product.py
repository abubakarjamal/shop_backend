from datetime import datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ProductCreate(BaseModel):
    name: str
    expiry_date: Optional[datetime] = None
    buying_price: Decimal
    selling_price: Decimal
    quantity_in_stock: int = 0
    minimum_stock: int = 5
    unit: str


class ProductResponse(BaseModel):
    id: int
    name: str
    expiry_date: Optional[datetime]
    buying_price: Decimal
    selling_price: Decimal
    quantity_in_stock: int
    minimum_stock: int
    unit: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
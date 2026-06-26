from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate


class ProductService:

    @staticmethod
    def create_product(db: Session, product: ProductCreate):
        if product.selling_price < product.buying_price:
            raise HTTPException(
                status_code=400,
                detail="Selling price cannot be lower than buying price."
            )

        return ProductRepository.create(db, product)
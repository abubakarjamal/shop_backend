from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


class ProductRepository:

    @staticmethod
    def create(db: Session, product: ProductCreate) -> Product:
        db_product = Product(**product.model_dump())

        db.add(db_product)
        db.commit()
        db.refresh(db_product)

        return db_product
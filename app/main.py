from fastapi import FastAPI

from app.database.base import Base
from app.database.session import engine

# Import models so SQLAlchemy knows about them
from app.models.product import Product
from app.models.sale import Sale
from app.models.sale_item import SaleItem

from app.api.products import router as product_router


Base.metadata.create_all(bind=engine)


app = FastAPI(title="Shop Management API")

app.include_router(product_router)


@app.get("/")
def root():
    return {"message": "Shop Management API is running"}
from pydantic import BaseModel


class ProductIn(BaseModel):
    name: str
    quantity: int
    price: float


class ProductUpdate(BaseModel):
    quantity: int
    price: float


class ProductOut(ProductIn):
    id: str)

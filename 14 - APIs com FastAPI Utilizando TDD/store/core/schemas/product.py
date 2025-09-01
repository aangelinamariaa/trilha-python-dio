from decimal import Decimal
from pydantic import BaseModel, Field
from base import BaseMoldel, BaseSchemaMixIn
from datetime import datetime
from uuid import UUID4


class ProductBase(BaseModel):
    name: str = Field(description="Nome do Produto")
    price: Decimal = Field(description="Preço do Produto")
    quantity: int = Field(description="Quantidade do Produto")
    status: bool = Field(description="Status do Produto")


class ProductIn(ProductBase, BaseSchemaMixIn):
    ...


class ProductOut(ProductIn):
    id: UUID4 = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    

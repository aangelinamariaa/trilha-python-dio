from pydantic import BaseModel, UUID4, Field
from datetime import datetime
from typing import Annotated


class BaseSchema(BaseModel):
    class Config:
        extra = "forbid"
        from_attributes = True


class OutMixinSchema(BaseModel):
    id: Annotated[UUID4, Field(description='Identificador')]
    created_at: Annotated[datetime, Field(description='Data da criação')]
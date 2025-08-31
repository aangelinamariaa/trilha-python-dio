from typing import Annotated
from pydantic import Field, UUID4
from workout_api.resources.schemas import BaseSchema


class CategoriaIn(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example="Scale", max_length=10)]


class CategoriaOut(CategoriaIn):
    id: Annotated[UUID4, Field(description="Identificador único da categoria")]
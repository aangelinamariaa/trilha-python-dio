from typing import Annotated
from pydantic import Field
from workout_api.resources.schemas import BaseSchema


class Categoria(BaseSchema):
    nome: Annotated[str, Field(description="Nome do Centro de Treinamento", example="CT King", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do Centro de Treinamento", example="", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietario do Centro de Treinamento", example="", max_length=30)]
from typing import Annotated
from pydantic import Field, UUID, BaseModel, PositiveFloat
from workout_api.resources.schemas import BaseSchema, OutMixin
from datetime import datetime




class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example="Scale", max_length=10)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678900", max_length=11)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]
    idade: Annotated[int, Field(description="Idade do atleta", example=25)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=75.5)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.70)]


class AtletaIn(Atleta):
    pass


class AtletaOut(Atleta, OutMixin):
    pass
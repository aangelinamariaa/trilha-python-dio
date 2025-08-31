from workout_api.resources.models import BaseSchema
from sqlalchemy import Integer, String, Float, DateTime
from sqlalchemy.orm import Mapped, mapped_column,relationship
from datetime import datetime


class CentroTreinamentoModel(BaseSchema):
    __tablename__ = "centro_treinamento"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)

    nome: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    telefone: Mapped[str] = mapped_column(String(20), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), nullable=False)
    proprietario: Mapped[str] = mapped_column(String(30), nullable=False)



    atleta: Mapped["AtletaModel"] = relationship(back_populates="centro_treinamento")
from uuid import uuid4
from fastapi import APIRouter, status, Body
from workout_api.resources.repository.dependencies import DatabaseDependency
from workout_api.categoria.schemas import CategoriaIn, CategoriaOut
from workout_api.categoria.model import CategoriaModel



router = APIRouter()


@router.post(
    '/',
    summary='Criar uma nova categoria',
    status_code=status.HTTP_201_CREATED,
    response_model=CategoriaOut,
)
async def post(
    db_session: DatabaseDependency,
    categoria_in: CategoriaIn = Body(...)
) -> CategoriaOut:    
    categoria_out = CategoriaOut(id=uuid4(), **categoria_in.model_dump())
    categoria_model = CategoriaModel(**categoria_out.model_dump())
    db_session.add(categoria_model)
    pass
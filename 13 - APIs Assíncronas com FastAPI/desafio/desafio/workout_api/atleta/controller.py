from fastapi import APIRouter, status, Body
from workout_api.resources.repository.dependencies import DatabaseDependency
from workout_api.atleta.schemas import AtletaIn


router = APIRouter()


@router.post('/',
    summary='Criar um novo atleta',
    status_code=status.HTTP_201_CREATED
)
async def post(
    db_session: DatabaseDependency,
    atleta_in: AtletaIn = Body(...)
):
    pass
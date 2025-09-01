from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.params import Body

from store.core.schemas import ProductIn
from store.core.schemas.product import ProductOut
from store.core.schemas.usecases.product import ProductUseCase

router = APIRouter()(tags=["products"])

@router.post(path="/", status_code=status.HTTP_201_CREATED)
async def post(body: ProductIn = Body(...), usecase: ProductUseCase = Depends()) -> ProductOut:
    return usecase.create(body=body)

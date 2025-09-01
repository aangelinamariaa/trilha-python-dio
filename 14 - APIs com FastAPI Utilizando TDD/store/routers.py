from fastapi import APIRouter, HTTPException, status

from store.core.schemas.usecases import product

api_router = APIRouter()
api_router.include_router(product)
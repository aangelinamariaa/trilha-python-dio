from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from store.db.mongo import db_client
from store.core.schemas.product import ProductIn, ProductOut
from uuid import UUID4


class ProductUseCase:
    def __init__(self) -> None:
        self.client: AsyncIOMotorClient = db_client.get()
        self.database = AsyncIOMotorDatabase(self.client.get_database())

    async def create(self, body: ProductIn) -> ProductOut:
        product = ProductOut(**body.model_dump())     
        await self.collection.insert_one(product.model_dump())

        return product

    async def get(self, id: UUID4) -> ProductOut:
        result = await self.collection.find_one({"id": id})

        return ProductOut(**result)


product_usecase = ProductUseCase()

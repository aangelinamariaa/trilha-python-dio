from motor.motor_asyncio import AsyncIOMotorClient

from store.core.config import settings


class MongoClient:
    def __init__(self, db_name: str):
        self.client: AsyncIOMotorClient = AsyncIOMotorClient()

    def get(self) -> AsyncIOMotorClient:
        return self.client
    

db_client = MongoClient("mongodb://localhost:27017/store?uuidRepresentation=standard")

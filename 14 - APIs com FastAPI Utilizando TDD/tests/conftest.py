import asyncio
import pytest
from store.db.mongo import db_client
from httpx import AsyncClient


@pytest.fixture(scope="session")
def event_lopp():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

@pytest.fixture
def mongo_client():
    return db_client.get()

@pytest.fixture
async def clear_collection():
    yield
    collections_names = await mongo_client.get.database().list_collection_names()
    for name in collections_names:
        if name.startswith("system"):
            continue
            
        await mongo_client.get.database()[name].delete_many({})

@pytest.fixture
async def client() -> AsyncClient:
    from store.main import app

    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac

@pytest.fixture
def product_url() -> str:
    return "/products/"

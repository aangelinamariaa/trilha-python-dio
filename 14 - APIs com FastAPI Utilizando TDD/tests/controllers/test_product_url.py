from tests.factories import product_data
from fastapi import status

async def test_controller_create_should_return_success(client, product_url):
    response = await client.post(produts_url, json=product_data())

    assert response.status_code == status.HTTP_201_CREATED
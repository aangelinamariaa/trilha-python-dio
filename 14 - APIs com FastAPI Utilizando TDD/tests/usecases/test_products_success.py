from store.core.schemas.product import ProductOut
from store.core.schemas.usecases.product import product_usecase


async def test_usecases_create_should_return_success(product_in):
    result = await product_usecase.create(product_in=product_in)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"


async def test_usecases_get_should_return_success(product_id, product_inserted):
    result = await product_usecase.get(id=product_id)

    assert isinstance(result, ProductOut)
    assert result.name == "Iphone 14 pro max"

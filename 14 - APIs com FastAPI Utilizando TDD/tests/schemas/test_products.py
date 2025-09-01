from store.core.schemas.product import ProductIn


def test_schema_validated():
    product = ProductIn(name="Iphone 14 pro max", quantity=10, price=8500.0, status=True)

    assert product.name == "Iphone 14 pro max"


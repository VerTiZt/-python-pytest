import pytest
from gamy_product import GamyProduct


# Фикстура для создания экземпляра GamyProduct
@pytest.fixture
def gamy_product():
    return GamyProduct(100.0)


# Параметризованный тест для проверки корректного вычисления цены со скидкой
@pytest.mark.parametrize("sale, expected_price", [
    (10, 90.0),
    (20, 80.0),
    (50, 50.0),
    (100, 0.0)
])
def test_price_with_a_sale(gamy_product, sale, expected_price):
    assert gamy_product.price_with_a_sale(sale) == expected_price


# Тест для проверки создания экземпляра с некорректной ценой
def test_invalid_price():
    with pytest.raises(ValueError, match="Invalid price"):
        GamyProduct(0.005)  # Некорректная цена

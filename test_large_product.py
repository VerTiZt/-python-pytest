import pytest
from large_product import LargeProduct


# Фикстура для создания экземпляра LargeProduct
@pytest.fixture
def large_product():
    return LargeProduct(10.0)  # Создаем экземпляр с корректным весом


# Тест для проверки создания экземпляра с некорректным весом
def test_invalid_weight():
    with pytest.raises(ValueError, match='Weight cannot be some negative number'):
        LargeProduct(-5.0)  # Некорректный вес


# Тест для проверки корректного вычисления ёмкости
def test_capacity(large_product):
    volume = large_product.capacity(2, 3, 4)  # Пример с размерами 2, 3, 4
    expected_capacity = (2 * 3 * 4) // large_product.weight  # Ожидаемая ёмкость
    assert volume == expected_capacity


# Тест для проверки ёмкости с другим набором значений
def test_capacity_with_different_values():
    product = LargeProduct(5.0)  # Создаем экземпляр с весом 5
    volume = product.capacity(10, 10, 10)  # Пример с размерами 10, 10, 10
    expected_capacity = (10 * 10 * 10) // product.weight  # Ожидаемая ёмкость
    assert volume == expected_capacity

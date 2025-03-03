import pytest
from product import Product


# Фикстура для создания экземпляра Product
@pytest.fixture
def product():
    return Product("Test Product", 100.0, 10, 20, 30)


# Параметризованный тест для проверки корректного вычисления цены со скидкой
@pytest.mark.parametrize("sale, expected_price", [
    (10, 90.0),
    (20, 80.0),
    (50, 50.0),
    (100, 0.0)
])
def test_price_with_a_sale(product, sale, expected_price):
    assert product.price_with_a_sale(sale) == expected_price


# Тест для проверки возможности сложения продуктов
def test_add_products(product):
    other_product = Product("Other Product", 50.0, 5, 10, 15)
    combined_product = product + other_product
    assert combined_product.price == 150.0
    assert combined_product.name == ''


# Тест для проверки загрузки продукта из файла
def test_load_from_file(monkeypatch):
    # Создаем временный файл с тестовыми данными
    test_data = "Test Product,100.0,10,20,30\n"
    with open('test_product.txt', 'w', encoding='UTF-8') as f:
        f.write(test_data)

    loaded_product = Product.load_from_file('test_product.txt')
    assert loaded_product.name == "Test Product"
    assert loaded_product.price == 100.0
    assert loaded_product.w == 10
    assert loaded_product.h == 20
    assert loaded_product.d == 30


# Тест для проверки сохранения продукта в файл
def test_save_to_file(product):
    product.save_to_file('test_save_product.txt')

    with open('test_save_product.txt', 'r', encoding='UTF-8') as f:
        line = f.readline().strip()
        assert line == "Test Product,100.0,10.0,20.0,30.0"


# Тест для проверки несуществующего файла
def test_load_from_nonexistent_file():
    with pytest.raises(FileNotFoundError):
        Product.load_from_file('nonexistent_file.txt')


# Тест для проверки некорректных данных
def test_load_from_file_with_incorrect_data(monkeypatch):
    # Создаем временный файл с некорректными данными
    incorrect_data = "Test Product,invalid_price,10,20,30\n"
    with open('incorrect_product.txt', 'w', encoding='UTF-8') as f:
        f.write(incorrect_data)

    with pytest.raises(ValueError):
        Product.load_from_file('incorrect_product.txt')


# Тест для проверки некорректной цены
def test_invalid_price():
    with pytest.raises(ValueError, match="Invalid price"):
        Product("Invalid Product", 0.005, 10, 10, 10)  # Некорректная цена

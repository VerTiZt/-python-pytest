from product import Product


class GamyProduct(Product):
    def __init__(self, price):
        super().__init__('', price, 0, 0, 0)

    def price_with_a_sale(self, sale: int) -> float:
        self.price_result = self.price * (1 - sale / 100)
        return round(self.price_result, 2)

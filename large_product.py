from product import Product


class LargeProduct(Product):
    def __init__(self, weight):
        super().__init__('', weight, 0, 0, 0)
        if weight < 0:
            raise ValueError('Weight cannot be some negative number')
        self.weight = weight

    def capacity(self, a, b, c) -> int:
        volume = a * b * c
        return volume // self.weight

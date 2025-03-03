class Product:
    price_result = 0.0
    weight = 0.0
    name = ''
    w, h, d = 0, 0, 0
    price = 0

    def __init__(self, name: str, price, w, h, d):
        if price < 0.01:
            raise ValueError('Invalid price')
        self.price = price
        self.name = name
        self.w = w
        self.h = h
        self.d = d

    def price_with_a_sale(self, sale: int) -> float:
        self.price_result = self.price * (1 - sale / 100)
        return round(self.price_result, 2)

    def __add__(self, other):
        if not isinstance(other, Product):
            return
        return Product('', self.price + other.price, 0, 0, 0)

    # 5 лаба
    @classmethod
    def load_from_file(cls, filename):
        try:
            with open(filename, 'r', encoding='UTF-8') as f:
                line = f.readline().strip()
                name, price, w, h, d = line.split(',')
                return cls(name, float(price), float(w), float(h), float(d))
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл '{filename}' не найден.")
        except ValueError as e:
            raise ValueError(f"Некорректные данные в файле: {e}")
        except IOError as e:
            raise RuntimeError(f"Ошибка чтения файла: {e}")

    def save_to_file(self, filename):
        try:
            with open(filename, 'w', encoding="UTF-8") as f:
                f.write(f"name: {self.name}, price: {self.price}, weight: {self.w}, height: {self.h}, shirina: {self.d}\n")
        except IOError as e:
            raise RuntimeError(f"Ошибка записи в файл: {e}")

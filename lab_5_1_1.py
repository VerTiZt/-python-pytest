from product import Product
from gamy_product import GamyProduct
from large_product import LargeProduct

if __name__ == '__main__':
    pr = Product(name='', price=0.1, w=0.1, h=0.1, d=0.1).load_from_file('products3.txt')
    sl = GamyProduct(price=20)
    am = LargeProduct(weight=100)
    res_sale1 = pr.price_with_a_sale(20)
    print(f'Price with a first sale: {res_sale1}')

    res_sale2 = sl.price_with_a_sale(20)
    print(f'Price with a second sale: {res_sale2}')

    res_amount = am.capacity(10, 10, 10)
    print(f'The box fill with: {res_amount}')

    summ = pr + sl
    print(f'Overload: {summ.price}')
    pr.save_to_file('products2.txt')

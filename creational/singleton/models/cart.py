# models/cart.py using singleton pattern
class Cart:

    def __init__(self):
        self.products = []
        self._total_value = 0

    def add_product(self, product):
        self.products.append(product)

    def total(self):
        return sum(p.price for p in self.products)

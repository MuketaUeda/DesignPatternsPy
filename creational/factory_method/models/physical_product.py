from .product import Product

class PhysicalProduct(Product):
    def __init__(self, name, price, weight=0.5):
        super().__init__(name, price)
        self.weight = weight

    def get_description(self):
        return f"Produto Físico: {self.name} - Peso: {self.weight}kg"
    
    def calculate_shipping(self):
        return self.weight * 10  # R$10 por kg
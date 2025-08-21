from .product import Product

class DigitalProduct(Product):
    def __init__(self, name, price, file_size=0):
        super().__init__(name, price)
        self.file_size = file_size

    def get_description(self):
        return f"Produto Digital: {self.name} - Tamanho: {self.file_size}MB"
    
    def calculate_shipping(self):
        return 0
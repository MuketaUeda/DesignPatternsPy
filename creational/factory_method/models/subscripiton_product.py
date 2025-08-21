from .product import Product

class SubscriptionProduct(Product):
    def __init__(self, name, price, duration_months = "monthly"):
        super().__init__(name, price)
        self.duration_months = duration_months

    def get_description(self):
        return f"Assinatura: {self.name} - Duração: {self.duration_months} meses"
    
    def calculate_shipping(self):
        return 0
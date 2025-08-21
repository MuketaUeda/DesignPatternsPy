from .physical_product import PhysicalProduct
from .digital_product import DigitalProduct
from .subscripiton_product import SubscriptionProduct

class ProductFactory:
    def create_product(self, product_type, name, price, **kwargs):
        if product_type == "physical":
            return PhysicalProduct(name, price, kwargs.get("weight", 1))
        elif product_type == "digital":
            return DigitalProduct(name, price, kwargs.get("file_size", 100))
        elif product_type == "subscription":
            return SubscriptionProduct(name, price, kwargs.get("duration_months", "monthly"))
        else:
            raise ValueError(f"Tipo de produto inválido: {product_type}")
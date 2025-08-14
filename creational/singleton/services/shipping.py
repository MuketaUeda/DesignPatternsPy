# services/shipping.py
class ShippingService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ShippingService, cls).__new__(cls)
        return cls._instance

    def ship(self, address):
        print(f"Enviando pedido para {address}")

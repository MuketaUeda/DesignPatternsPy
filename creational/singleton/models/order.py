# models/order.py
class Order:
    def __init__(self, cart):
        self.cart = cart
        self.status = "Novo"

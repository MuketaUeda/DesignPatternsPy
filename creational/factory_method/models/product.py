# models/product.py
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def calculate_shipping(self):
        pass


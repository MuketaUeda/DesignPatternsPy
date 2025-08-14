# services/payment.py
class PaymentService:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PaymentService, cls).__new__(cls)
        return cls._instance

    def pay(self, method, amount):
        if method == "pix":
            print(f"Pagando R${amount} via PIX...")
        elif method == "cartao":
            print(f"Pagando R${amount} no cartão...")
        else:
            print("Método de pagamento inválido.")

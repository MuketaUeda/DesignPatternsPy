# services/payment.py
class PaymentService:
    def pay(self, method, amount):
        if method == "pix":
            print(f"Pagando R${amount} via PIX...")
        elif method == "cartao":
            print(f"Pagando R${amount} no cartão...")
        else:
            print("Método de pagamento inválido.")

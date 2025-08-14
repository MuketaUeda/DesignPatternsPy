# main.py
from models.product import Product
from models.cart import Cart
from services.payment import PaymentService
from services.shipping import ShippingService
from services.notification import NotificationService

def main():
    # Criar produtos
    p1 = Product("Camiseta", 50)
    p2 = Product("Tênis", 200)

    # Criar carrinho e adicionar produtos
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p2)

    # Calcular total
    print(f"Total do carrinho: R${cart.total()}")

    # Pagamento (ingênuo - sem padrões)
    payment_service = PaymentService()
    payment_service.pay("pix", cart.total())

    # Envio (ingênuo)
    shipping_service = ShippingService()
    shipping_service.ship("Rua ABC, 123")

    # Notificação (ingênuo)
    notification_service = NotificationService()
    notification_service.send_email("cliente@email.com", "Pedido enviado!")

if __name__ == "__main__":
    main()

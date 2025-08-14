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
    payment_service2 = PaymentService()
    print(f"PaymentService é singleton? {payment_service is payment_service2}")
    print(payment_service)
    print(payment_service2)
    payment_service.pay("pix", cart.total())

    # Envio (ingênuo)
    shipping_service = ShippingService()
    shipping_service.ship("Rua ABC, 123")

    # Notificação (singleton)
    notification_service = NotificationService()
    notification_service2 = NotificationService()
    print(f"NotificationService é singleton? {notification_service is notification_service2}")
    print(notification_service)
    print(notification_service2)
    notification_service.send_email("cliente@email.com", "Pedido enviado!")

if __name__ == "__main__":
    main()

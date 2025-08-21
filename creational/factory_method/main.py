# main.py
from models.product_factory import ProductFactory
from models.cart import Cart
from services.payment import PaymentService
from services.shipping import ShippingService
from services.notification import NotificationService

def main():
    # Criar produtos
    physical_p = ProductFactory().create_product("physical", "Camiseta", 50, weight=0.5)
    digital_p = ProductFactory().create_product("digital", "Tênis", 200, file_size=100)
    subscription_p = ProductFactory().create_product("subscription", "Assinatura", 100, duration_months=12)

    for product in [physical_p, digital_p, subscription_p]:
        print(product.get_description())
        print(f"Frete: R${product.calculate_shipping()}")
        print(f"Preço: R${product.price}")
        print(f"Total: R${product.price + product.calculate_shipping()}")
        print("-" * 40)

    # Criar carrinho e adicionar produtos
    cart = Cart()
    cart.add_product(physical_p)
    cart.add_product(digital_p)
    cart.add_product(subscription_p)

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

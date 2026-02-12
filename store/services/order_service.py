from store.models import Order, OrderItem
from decimal import Decimal

class PaymentStrategy:
    def pay(self, order, payment_info):
        raise NotImplementedError

class PixPayment(PaymentStrategy):
    def pay(self, order, payment_info):
        order.status = "paid"
        order.save(update_fields=["status"])

class OrderService:
    def __init__(self, payment_strategy: PaymentStrategy = None):
        self.payment_strategy = payment_strategy or PixPayment()

    def create_order(self, user, cart_service, checkout_data):
        items = cart_service.items()
        total = cart_service.total()
        order = Order.objects.create(
            user=user,
            first_name=checkout_data.get("first_name"),
            last_name=checkout_data.get("last_name"),
            email=checkout_data.get("email"),
            address=checkout_data.get("address"),
            city=checkout_data.get("city"),
            zip_code=checkout_data.get("zip_code"),
            total_paid=Decimal(total),
            status="pending",
        )
        for item in items:
            product = item["product"]
            quantity = item["quantity"]
            if product.stock < quantity:
                order.delete()
                raise ValueError(f"Estoque insuficiente para {product.name}")
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                price=product.price,
            )
            product.stock -= quantity
            product.save(update_fields=["stock"])
        return order

    def confirm_payment(self, order, payment_info=None):
        self.payment_strategy.pay(order, payment_info or {})
        return order
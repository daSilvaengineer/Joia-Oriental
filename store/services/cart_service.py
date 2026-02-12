from decimal import Decimal
from store.models import Product

class CartService:
    SESSION_KEY = "cart"

    def __init__(self, session):
        self.session = session
        cart = self.session.get(self.SESSION_KEY)
        if not cart:
            cart = self.session[self.SESSION_KEY] = {}
        self.cart = cart

    def add_product(self, product_id, quantity=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {"quantity": 0}
        self.cart[product_id]["quantity"] += quantity
        self.save()

    def remove_product(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def clear(self):
        if self.SESSION_KEY in self.session:
            del self.session[self.SESSION_KEY]
        self.cart = {}
        self.save()

    def items(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        cart_items = []
        for product in products:
            item_data = self.cart.get(str(product.id))
            quantity = item_data["quantity"]
            cart_items.append({
                "product": product,
                "quantity": quantity,
                "subtotal": Decimal(str(product.price)) * quantity
            })
        return cart_items

    def total(self):
        return sum(
            (item["subtotal"] for item in self.items()),
            Decimal("0.00")
        )

    def count(self):
        return sum(item["quantity"] for item in self.cart.values())

    def save(self):
        self.session.modified = True
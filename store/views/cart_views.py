from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.services.cart_service import CartService
from store.models import Product

@login_required
def cart_detail(request):
    cart_service = CartService(request.session)
    return render(
        request,
        "store/pages/cart.html",
        {
            "items": cart_service.items(),
            "total": cart_service.total(),
            "count": cart_service.count(),
        }
    )

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_service = CartService(request.session)
    cart_service.add_product(product_id, quantity=1)
    messages.success(request, f"{product.name} adicionado ao carrinho.")
    return redirect(request.META.get('HTTP_REFERER', 'store:home'))

@login_required
def remove_from_cart(request, product_id):
    cart_service = CartService(request.session)
    cart_service.remove_product(product_id)
    return redirect("store:cart_detail")
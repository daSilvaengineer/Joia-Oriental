from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Order
from store.services.cart_service import CartService
from store.services.order_service import OrderService
from store.forms.checkout_form import CheckoutForm

@login_required
def checkout(request):
    cart_service = CartService(request.session)
    items = cart_service.items()
    if not items:
        messages.error(request, "Seu carrinho está vazio.")
        return redirect("store:cart_detail")
    if request.method == "POST":
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order_service = OrderService()
            try:
                order = order_service.create_order(
                    user=request.user,
                    cart_service=cart_service,
                    checkout_data=form.cleaned_data,
                )
                cart_service.clear()
                return redirect("store:payment_choice", order_id=order.id)
            except ValueError as e:
                messages.error(request, str(e))
                return redirect("store:checkout")
        messages.error(request, "Corrija os dados de entrega.")
    else:
        form = CheckoutForm(initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
        })
    return render(
        request,
        "store/pages/checkout.html",
        {
            "items": items,
            "total": cart_service.total(),
            "form": form,
        }
    )

@login_required
def payment_choice(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    if order.status.lower() != "pending":
        messages.error(request, "Pedido já processado ou inválido.")
        return redirect("store:order_history")
    if request.method == "POST":
        method = request.POST.get("method")
        order_service = OrderService()
        if method in ["pix", "pix_discount"]:
            order_service.confirm_payment(order)
            messages.success(request, "Pagamento confirmado com sucesso!")
            return redirect("store:order_history")
        messages.error(request, "Método de pagamento inválido.")
    return render(
        request,
        "store/pages/payment_choice.html",
        {"order": order}
    )

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-id')
    return render(
        request,
        "store/pages/order_history.html",
        {"orders": orders}
    )
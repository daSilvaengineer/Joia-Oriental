from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from store.models import Order


@login_required
def profile(request):
    """
    Página de perfil do usuário.
    """
    orders = Order.objects.filter(user=request.user).order_by("-created_at")

    return render(
        request,
        "store/pages/profile.html",
        {
            "orders": orders,
        }
    )

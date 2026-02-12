from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from store.forms.auth_form import RegistroForm
from store.models import Order


# -------------------------
# LOGIN
# -------------------------
class CustomLoginView(LoginView):
    template_name = "store/auth/login.html"

    def form_invalid(self, form):
        messages.error(self.request, "Credenciais inválidas.")
        return super().form_invalid(form)


# -------------------------
# LOGOUT
# -------------------------
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("store:home")

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, "Você saiu da sua conta.")
        return super().dispatch(request, *args, **kwargs)


# -------------------------
# SIGNUP
# -------------------------
def signup(request):
    form = RegistroForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Cadastro realizado! Faça login.")
            return redirect("store:login")
        else:
            messages.error(request, "Corrija os erros abaixo.")

    return render(request, "store/auth/signup.html", {"form": form})


# -------------------------
# PROFILE
# -------------------------
@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "store/pages/profile.html", {"orders": orders})

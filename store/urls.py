from django.urls import path
from .views import (
    product_views,
    cart_views,
    profile_views,
    auth_views,
    order_views,
    collection_views,
    about_views,
)


app_name = "store"

urlpatterns = [
    path("", product_views.home_page, name="home"),
    path("product/<slug:slug>/", product_views.product_detail, name="product_detail"),

    path("cart/", cart_views.cart_detail, name="cart_detail"),
    path("cart/add/<int:product_id>/", cart_views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<int:product_id>/", cart_views.remove_from_cart, name="remove_from_cart"),

    path("login/", auth_views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.CustomLogoutView.as_view(), name="logout"),
    path("signup/", auth_views.signup, name="signup"),

    path("profile/", profile_views.profile, name="profile"),

    path("checkout/", order_views.checkout, name="checkout"),
    path("payment/<int:order_id>/", order_views.payment_choice, name="payment_choice"),
    path("history/", order_views.order_history, name="order_history"),

   
    path("collections/", collection_views.collections_page, name="collections"),
    path("about/", about_views.about_page, name="about"),


]

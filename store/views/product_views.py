from django.shortcuts import render, get_object_or_404
from store.models import Product, Category


def home_page(request):
    """
    Página inicial – Joia Oriental
    Usa layout modular com components.
    """

    products = Product.objects.all()
    featured_products = products.filter(is_featured=True)[:8]
    categories = Category.objects.all()

    return render(
        request,
        "store/pages/home.html",
        {
            "products": products,
            "featured_products": featured_products,
            "categories": categories,
        }
    )


def product_detail(request, slug):
    """
    Página de detalhes da joia.
    """

    product = get_object_or_404(Product, slug=slug)

    related_products = (
        Product.objects
        .filter(category=product.category)
        .exclude(id=product.id)[:4]
    )

    return render(
        request,
        "store/pages/product_detail.html",
        {
            "product": product,
            "related_products": related_products,
        }
    )

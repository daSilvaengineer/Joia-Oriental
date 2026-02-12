from .services.cart_service import CartService

def cart_context(request):
    if not hasattr(request, 'session'):
        return {'cart_count': 0}
        
    cart_service = CartService(request.session)
    return {
        'cart_count': cart_service.count()
    }
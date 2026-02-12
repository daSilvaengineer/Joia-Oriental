from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Product, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'display_image']
    prepopulated_fields = {'slug': ('name',)}

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "Sem imagem"
    display_image.short_description = 'Capa'

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['display_image', 'name', 'category', 'price', 'stock', 'is_featured']
    list_filter = ['is_featured', 'category', 'material', 'created_at']
    list_editable = ['price', 'stock', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description']

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto; border-radius: 5px;" />', obj.image.url)
        return "Sem imagem"
    display_image.short_description = 'Miniatura'

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    readonly_fields = ['product', 'price', 'quantity', 'get_subtotal']
    
    def get_subtotal(self, obj):
        return obj.get_subtotal()
    get_subtotal.short_description = 'Subtotal'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'first_name', 'status', 'total_paid', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['first_name', 'last_name', 'email']
    inlines = [OrderItemInline]
    readonly_fields = ['total_paid', 'created_at']
    
    # Organizando os campos em seções (Fieldsets)
    fieldsets = (
        ('Informações do Cliente', {
            'fields': ('user', 'first_name', 'last_name', 'email')
        }),
        ('Endereço de Entrega', {
            'fields': ('address', 'city', 'zip_code')
        }),
        ('Status e Pagamento', {
            'fields': ('status', 'total_paid', 'created_at')
        }),
    )
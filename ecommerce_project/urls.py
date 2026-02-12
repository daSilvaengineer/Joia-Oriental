from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔥 ROTAS DO ALLAUTH (Google/Facebook/Login Social)
    path('accounts/', include('allauth.urls')),

    # SUAS ROTAS DO E-COMMERCE
    path('', include('store.urls')),
]

# Servir apenas MEDIA em desenvolvimento (STATIC já é servido pelo Django automaticamente)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

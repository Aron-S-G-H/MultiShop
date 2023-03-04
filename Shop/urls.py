from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from Shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('product_app.urls')),
    path('account/', include('account_app.urls')),
    path('basket/', include('basket_app.urls')),
    path('contactUs/', include('contact_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

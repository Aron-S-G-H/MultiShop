from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.Home.as_view(), name='home_page'),
    path('shop', views.Shop.as_view(), name='shop_page'),
    path('product/<slug:slug>', views.ProductDetailView.as_view(), name='productDetail_page'),
    path('category/<slug:slug>', views.CategoryDetail.as_view(), name='categoryDetail_page'),
    path('search', views.search, name='searchDetail_page'),
]

from django.urls import path
from . import views

app_name = 'basket'
urlpatterns = [
    path('detail', views.BasketDetailView.as_view(), name='details_page'),
    path('add/<int:pk>', views.BasketAddView.as_view(), name='addToBasket'),
    path('remove/<str:unique_id>', views.BasketRemoveView.as_view(), name='removeFromBasket'),
    path('checkout', views.CheckOutView.as_view(), name='checkOut_page'),
    path('orderlist/<int:pk>', views.OrderList.as_view(), name='ordersList_page'),
    path('applDiscount/<int:pk>', views.ApplyDiscountCode.as_view(), name='applyDiscount'),
    path('pdf/invoice/<int:order_id>', views.admin_invoice_pdf, name='admin_invoice_page')
]

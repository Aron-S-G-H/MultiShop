from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login', views.Login.as_view(), name='Login_page'),
    path('register', views.Register.as_view(), name='register_page'),
    path('checkotp', views.CheckOtp.as_view(), name='checkOtp_page'),
    path('logout', views.user_logout, name='logout_page'),
    path('update', views.user_edit, name='update_page'),
]

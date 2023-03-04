from django.apps import AppConfig


class BasketAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket_app'
    verbose_name = 'بخض سفارشات'

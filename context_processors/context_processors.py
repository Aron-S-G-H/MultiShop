from product_app.models import Category
from contact_app.models import ContactInfo
from basket_app.basket_module import Basket


def data_to_base(request):
    categories = Category.objects.all()
    infos = ContactInfo.objects.last()
    basket = Basket(request)
    return {'categories': categories, 'infos': infos, 'basket': basket}


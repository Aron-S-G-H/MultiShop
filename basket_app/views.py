from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from product_app.models import Product
from .basket_module import Basket
from .forms import CheckoutForm
from .models import UserOrder, ProductOrder, DiscountCode
from django.contrib import messages
from datetime import datetime
import pytz
from django.template.loader import render_to_string
from django.contrib.admin.views.decorators import staff_member_required
import weasyprint
from django.conf import settings
from django.http import HttpResponse


class BasketDetailView(View):
    def get(self, request):
        basket = Basket(request)
        return render(request, 'basket_app/basket_detail.html', {'basket': basket})


class BasketAddView(View):
    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)
        size, color, quantity = request.POST.get('size'), request.POST.get('color'), request.POST.get('quantity')
        basket = Basket(request)
        basket.add(product, quantity, color, size)
        return redirect('basket:details_page')


class BasketRemoveView(View):
    def get(self, request, unique_id):
        basket = Basket(request)
        basket.delete(unique_id)
        return redirect('basket:details_page')


class CheckOutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            form = CheckoutForm(initial={'fullname': request.user.fullname,
                                         'email': request.user.email,
                                         'phone': f'0{request.user.phone}'})
            return render(request, 'basket_app/basket_checkout.html', {'form': form})
        else:
            return redirect('account:Login_page')

    def post(self, request):
        basket = Basket(request)
        form = CheckoutForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            order = UserOrder.objects.create(user=request.user, total_price=basket.total(), fullname=cd['fullname'],
                                             email=cd['email'],
                                             phone=cd['phone'],
                                             city=cd['city'],
                                             postal_code=cd['postal_code'],
                                             address=cd['address'])
            for item in basket:
                ProductOrder.objects.create(
                    order=order,
                    product=item['product'],
                    size=item['size'],
                    color=item['color'],
                    quantity=item['quantity'],
                    price=item['price']
                )
            basket.remove_cart()
            messages.success(request, 'سفارش شما با موفقیت ثبت شد, با پرداخت سفارش خود را نهایی کنید')
            return redirect('basket:ordersList_page', order.id)
        return render(request, 'basket_app/basket_checkout.html', {'form': form})


class OrderList(View):
    def get(self, request, pk):
        order = get_object_or_404(UserOrder, id=pk)
        return render(request, 'basket_app/order_list.html', {'order': order})


class ApplyDiscountCode(View):
    def post(self, request, pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(UserOrder, id=pk)
        if not code:
            messages.error(request, 'کد تخفیف را وارد کنید')
        else:
            try:
                discount_code = DiscountCode.objects.get(name_id=code)
                utc = pytz.UTC
                now = datetime.now().replace(tzinfo=utc)
                expiration_date = discount_code.expiration_date.replace(tzinfo=utc)
            except:
                messages.error(request, 'کد تخفیف معتبر نیست')
                return redirect('basket:ordersList_page', order.id)

            if request.user in discount_code.used_by.all():
                messages.error(request, 'شما از کد تخفیف استفاده کردید')
                return redirect('basket:ordersList_page', order.id)

            while True:
                if not discount_code.status:
                    messages.error(request, 'Discount Code does not Exist')
                    break
                elif discount_code.quantity == 0:
                    discount_code.status = False
                    discount_code.save()
                    continue
                elif now == expiration_date or now > expiration_date:
                    discount_code.status = False
                    discount_code.save()
                    continue
                else:
                    order.total_price -= (order.total_price * discount_code.percent) / 100
                    order.save()
                    discount_code.quantity -= 1
                    discount_code.used_by.add(request.user)
                    discount_code.save()
                    break
        return redirect('basket:ordersList_page', order.id)


@staff_member_required
def admin_invoice_pdf(request, order_id):
    order = get_object_or_404(UserOrder, id=order_id)
    html = render_to_string('basket_app/invoice_pdf.html', {'order': order})
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'FileName = order_{order.id}.pdf'
    weasyprint.HTML(string=html).write_pdf(response, stylesheets=[weasyprint.CSS(
        settings.STATIC_ROOT + '/css/invoice.css'
    )])
    return response

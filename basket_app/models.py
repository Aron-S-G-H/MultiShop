from django.db import models
from django.core.validators import MaxValueValidator
from userModel_app.models import User
from product_app.models import Product
from datetime import datetime, timedelta


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='کاربر')
    fullname = models.CharField(max_length=40, verbose_name='نام کامل', null=True)
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(verbose_name='شماره همراه', max_length=11)
    city = models.CharField(verbose_name='شهر', max_length=30)
    postal_code = models.PositiveIntegerField(verbose_name='کد پستی')
    address = models.TextField(verbose_name='آدرس')
    total_price = models.PositiveIntegerField(verbose_name='هزینه کل', default=0)
    is_paid = models.BooleanField(verbose_name='وضعیت پرداخت', default=False)
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'


class ProductOrder(models.Model):
    order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items', verbose_name='محصول')
    size = models.CharField(verbose_name='اندازه محصول', max_length=5)
    color = models.CharField(verbose_name='رنگ', max_length=10)
    quantity = models.PositiveSmallIntegerField(verbose_name='تعداد')
    price = models.PositiveIntegerField(verbose_name='قیمت')

    def __str__(self):
        return self.product.product_name

    def get_cost(self):
        cost = self.quantity * self.price
        return cost

    class Meta:
        verbose_name = 'سفارش محصول'
        verbose_name_plural = 'سفارش محصولات'


class DiscountCode(models.Model):
    name_id = models.CharField(max_length=30, unique=True, verbose_name='شناسه کد تخفیف')
    percent = models.PositiveSmallIntegerField(default=1, verbose_name='درصد تخفیف', validators=[MaxValueValidator(100)])
    quantity = models.PositiveSmallIntegerField(default=1, verbose_name='تعداد کد')
    valid_from = models.DateTimeField(default=datetime.now(), verbose_name='تاریخ شروع اعتبار')
    validity = models.PositiveSmallIntegerField(default=1, verbose_name='اعتبار کد تخفیف', help_text='تعداد روزهایی که کد اعتبار دارد')
    expiration_date = models.DateTimeField(blank=True, verbose_name='تاریخ انتقضا', help_text='به صورت خودکار فیلد تکمیل و بعد از تاریخ به دست آمده کد منقضی میشود')
    status = models.BooleanField(default=True, verbose_name='فعال')
    used_by = models.ManyToManyField(User, verbose_name='استفاده شده توسط', blank=True)

    def __str__(self):
        return self.name_id

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.expiration_date = self.valid_from + timedelta(days=self.validity)
        super(DiscountCode, self).save()

    class Meta:
        verbose_name = 'کد تخفیف'
        verbose_name_plural = 'کد های تخفیف'

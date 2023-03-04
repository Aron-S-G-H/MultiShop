from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from userModel_app.models import User


class Category(models.Model):
    title = models.CharField(max_length=25, verbose_name='عنوان دسته بندی', unique=True)
    image = models.ImageField(upload_to='Cateory', verbose_name='تصویر دسته بندی')
    slug = models.SlugField(blank=True, verbose_name='اسلاگ', help_text='این فیلد به صورت خودکار تکمیل می شود')
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.title)
        super(Category, self).save()

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Size(models.Model):
    title = models.CharField(max_length=5, verbose_name='اندازه', unique=True)
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اندازه محصول'
        verbose_name_plural = 'اندازه محصولات'


class Color(models.Model):
    title = models.CharField(max_length=10, verbose_name='رنگ', unique=True)
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'رنگ محصول'
        verbose_name_plural = 'رنگ محصولات'


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='دسته بندی')
    product_name = models.CharField(max_length=30, verbose_name='اسم محصول')
    description = RichTextField(verbose_name='توضیحات')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    discount = models.PositiveSmallIntegerField(verbose_name='قیمت ویژه', blank=True, null=True)
    image = models.ImageField(upload_to='Product', verbose_name='تصویر محصول')
    size = models.ManyToManyField(Size, verbose_name='اندازه محصول', related_name='products')
    color = models.ManyToManyField(Color, verbose_name='رنگ محصول', related_name='products')
    feature_product = models.BooleanField(verbose_name='محصول ویژه', help_text='در صورت فعال بودن گزینه،این محصول در بخش محصولات ویژه نمایش داده می شود')
    status = models.BooleanField(verbose_name='وضعیت', help_text='وضعیت انتشار محصول در سایت', default=False)
    slug = models.SlugField(blank=True, verbose_name='اسلاگ', help_text='این فیلد به صورت خودکار تکمیل می شود')
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد محصول', auto_now_add=True)

    def __str__(self):
        return self.product_name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.product_name)
        super(Product, self).save()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'
        ordering = ('-created_at',)


class Option(models.Model):
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, verbose_name='محصول', related_name='options')
    text = models.TextField(verbose_name='ویژگی محصول')

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی محصولات'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name= 'کاربر',  null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments', verbose_name='محصول')
    name = models.CharField(max_length=20, verbose_name='نام و نام خانوادگی')
    email = models.EmailField(verbose_name='ایمیل')
    text = models.TextField(verbose_name='متن کامنت')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')

    def __str__(self):
        return self.text[:10]

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'بخش نظرات محصول'

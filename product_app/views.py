from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Product, Comment, Category, Color, Size
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages


class Home(View):
    def get(self, request):
        feature_products = Product.objects.filter(feature_product=True)[0:6]
        recent_products = Product.objects.order_by('-created_at')[0:6]
        return render(request, 'product_app/home.html',
                      {'feature_pro': feature_products, 'recent_pro': recent_products})


class Shop(View):
    def get(self, request):
        products = Product.objects.all()
        colors = Color.objects.all()
        sizes = Size.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(products, 9)
        products_list = paginator.get_page(page_number)
        return render(request, 'product_app/shop.html', {'products_list': products_list, 'colors': colors, 'sizes': sizes})

    def post(self, request):
        filter_color = request.POST.get('filter_color')
        filter_size = request.POST.get('filter_size')
        if filter_color:
            color_id = Color.objects.get(title=filter_color).id
            products = Product.objects.filter(color=color_id)
        else:
            size_id = Size.objects.get(title=filter_size).id
            products = Product.objects.filter(size=size_id)
        colors = Color.objects.all()
        sizes = Size.objects.all()
        page_number = request.GET.get('page')
        paginator = Paginator(products, 9)
        products_list = paginator.get_page(page_number)
        return render(request, 'product_app/shop.html', {'products_list': products_list, 'colors': colors, 'sizes': sizes})


class ProductDetailView(View):
    def get(self, request, slug):
        product = get_object_or_404(Product, slug=slug)
        category = get_object_or_404(Category, title=product.category)
        return render(request, 'product_app/product_detail.html', {'product': product, 'category': category})

    def post(self, request, slug):
        if request.user.is_authenticated:
            product = Product.objects.get(slug=slug)
            text = request.POST.get('text')
            name = request.user.fullname
            email = request.user.email
            Comment.objects.create(
                user=request.user,
                product=product,
                name=name,
                text=text,
                email=email,
            )
            date = str(Comment.objects.get(text=text).created_at.date()).replace('-', ' ')
            return JsonResponse({'status': 200, 'name': name, 'date': date})
        else:
            return JsonResponse({'status': 401})


def search(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        products = Product.objects.filter(product_name__icontains=query)
        if not products:
            messages.info(request, 'Nothing Found')
        page_number = request.GET.get('page')
        paginator = Paginator(products, 9)
        products_list = paginator.get_page(page_number)
        return render(request, 'product_app/search_detail.html', {'products_list': products_list})


class CategoryDetail(View):
    def get(self, request, slug):
        category = get_object_or_404(Category, slug=slug)
        products = category.products.all()
        page_number = request.GET.get('page')
        paginator = Paginator(products, 9)
        products_list = paginator.get_page(page_number)
        return render(request, 'product_app/category_detail.html', {'products_list': products_list, 'category': category})

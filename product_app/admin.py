from django.contrib import admin
from . import models


class OptionAdmin(admin.StackedInline):
    model = models.Option
    extra = 0


class CommentAdmin(admin.StackedInline):
    model = models.Comment
    readonly_fields = ('created_at',)
    extra = 0


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created_at')
    ordering = ('-created_at',)
    list_display = ('product_name', 'category', 'price', 'status', 'feature_product', 'created_at', 'image')
    list_filter = ('category', 'status', 'feature_product')
    search_fields = ('product_name',)
    inlines = (OptionAdmin, CommentAdmin)


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('slug', 'created_at')
    ordering = ('-created_at',)
    list_display = ('title', 'image','created_at')
    search_fields = ('title',)


class SizeColorAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
    list_display = ('title', 'created_at')
    search_fields = ('title',)


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Size, SizeColorAdmin)
admin.site.register(models.Color, SizeColorAdmin)

from django.contrib import admin
from . import models
from django.urls import reverse
from django.utils.safestring import mark_safe
import csv
from django.http import HttpResponse


def user_invoice_pdf(order):
    url = reverse('basket:admin_invoice_page', args=[order.id])
    return mark_safe(f'<a href="{url}">PDF</a>')


user_invoice_pdf.short_description = 'Export to PDF'


class ProductOrderAdmin(admin.TabularInline):
    model = models.ProductOrder
    extra = 0


@admin.register(models.UserOrder)
class UserOrderAdmin(admin.ModelAdmin):
    inlines = (ProductOrderAdmin,)
    list_filter = ('is_paid', 'city')
    list_display = ('id', 'user', 'phone', 'city', 'total_price', 'is_paid', user_invoice_pdf)
    readonly_fields = ('created_at',)
    search_fields = ('user', 'phone', 'postal_code', 'fullname')
    list_editable = ('total_price',)
    actions = ['export_as_csv']

    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta.verbose_name)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export as CSV"


@admin.register(models.DiscountCode)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name_id', 'percent', 'quantity', 'validity', 'status', 'expiration_date')
    list_filter = ('status',)
    search_fields = ('name_id',)
    readonly_fields = ('expiration_date',)
    list_editable = ('percent', 'quantity', 'validity', 'status')

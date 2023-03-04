from django.contrib import admin
from .models import ContactUs, ContactInfo, SendEmail
# Register your models here.


@admin.register(SendEmail)
class SendEmailAdmin(admin.ModelAdmin):
    readonly_fields = ('send_at', 'submit_status')
    list_display = ('user', 'subject', 'submit_status', 'send_at')
    list_filter = ('submit_status',)
    search_fields = ('user', 'subject')


class ContactUsAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'email', 'title', 'created_at')


class ContactInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('email', 'phone', 'address', 'short_description')


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)

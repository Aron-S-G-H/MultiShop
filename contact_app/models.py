from django.db import models
from userModel_app.models import User
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.validators import ValidationError


class ContactUs(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='messages')
    name = models.CharField(max_length=30, verbose_name='نام کامل')
    email = models.EmailField(verbose_name='ایمیل')
    title = models.CharField(max_length=50, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created_at = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'


class ContactInfo(models.Model):
    address = models.CharField(max_length=50, verbose_name='آدرس فروشگاه')
    email = models.EmailField(verbose_name='ایمیل')
    phone = models.CharField(max_length=11, verbose_name='شماره تماس')
    short_description = models.TextField(max_length=150, verbose_name='توضیح کوتاه')
    insta_link = models.CharField(max_length=50, verbose_name='لینک صفحه اینستاگرام')
    linkedin_link = models.CharField(max_length=50, verbose_name='لینک صفحه لینکدین')
    twitter_link = models.CharField(max_length=50, verbose_name='لینک صفحه توییتر')
    facebook_link = models.CharField(max_length=50, verbose_name='لینک صفحه فیسبوک')
    created_at = models.DateTimeField(verbose_name='تاریخ', auto_now=True)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'راه ارتباطی'
        verbose_name_plural = 'راه های ارتباطی'


class SendEmail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر', related_name='emails')
    subject = models.CharField(max_length=50, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام', blank=True, null=True)
    file = models.FileField(verbose_name='فایل', blank=True, null=True, upload_to='messages_file')
    send_at = models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال')
    submit_status = models.BooleanField(verbose_name='وضعیت ارسال پیام', blank=True)

    def __str__(self):
        return f'{self.user} | {self.subject}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        user_email = self.user.email
        if self.message and self.file:
            try:
                mail = EmailMessage(subject=self.subject, body=self.message, from_email=settings.EMAIL_HOST_USER, to=[user_email])
                mail.attach(self.file.url, self.file.read())
                mail.send()
                self.submit_status = True
                super(SendEmail, self).save()
            except:
                self.submit_status = False
                super(SendEmail, self).save()
        else:
            if self.message:
                message = self.message
                mail = EmailMessage(subject=self.subject, body=message, from_email=settings.EMAIL_HOST_USER, to=[user_email])
            elif self.file:
                message = self.file
                mail = EmailMessage(subject=self.subject, body='Your File', from_email=settings.EMAIL_HOST_USER, to=[user_email])
                mail.attach(message.url, message.read())
            else:
                raise ValidationError('حداقل یه پیام یا یک فایل برای ارسال انتخاب کنید')
            try:
                mail.send()
                self.submit_status = True
                super(SendEmail, self).save()
            except:
                self.submit_status = False
                super(SendEmail, self).save()

    class Meta:
        verbose_name = 'ارسال پیام به کاربر'
        verbose_name_plural = 'ارسال پیام به کاربران'


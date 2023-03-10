# Generated by Django 4.1.2 on 2023-02-13 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0002_alter_contactus_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, verbose_name='آدرس فروشگاه')),
                ('email', models.EmailField(max_length=254, verbose_name='ایمیل')),
                ('phone', models.CharField(max_length=11, verbose_name='شماره تماس')),
                ('short_description', models.TextField(max_length=100, verbose_name='توضیح کوتاه')),
                ('insta_link', models.CharField(max_length=50, verbose_name='لینک صفحه اینستاگرام')),
                ('linkedin_link', models.CharField(max_length=50, verbose_name='لینک صفحه لینکدین')),
                ('twitter_link', models.CharField(max_length=50, verbose_name='لینک صفحه توییتر')),
                ('facebook_link', models.CharField(max_length=50, verbose_name='لینک صفحه فیسبوک')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ')),
            ],
        ),
    ]

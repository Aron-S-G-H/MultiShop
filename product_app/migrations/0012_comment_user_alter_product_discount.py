# Generated by Django 4.1.2 on 2023-02-24 12:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product_app', '0011_alter_product_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='قیمت ویژه'),
        ),
    ]

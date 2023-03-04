# Generated by Django 4.1.2 on 2023-02-18 16:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0005_alter_discountcode_valid_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 18, 19, 40, 21, 607548), verbose_name='تاریخ شروع اعتبار'),
        ),
        migrations.AlterField(
            model_name='discountcode',
            name='validity',
            field=models.PositiveSmallIntegerField(default=1, help_text='تعداد روزهایی که کد اعتبار دارد', verbose_name='اعتبار کد تخفیف'),
        ),
    ]
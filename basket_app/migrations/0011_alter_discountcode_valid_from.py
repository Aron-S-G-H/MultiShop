# Generated by Django 4.1.2 on 2023-03-01 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0010_alter_discountcode_valid_from'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discountcode',
            name='valid_from',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 1, 20, 2, 37, 282495), verbose_name='تاریخ شروع اعتبار'),
        ),
    ]

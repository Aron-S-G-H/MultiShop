# Generated by Django 4.1.2 on 2023-02-07 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket_app', '0002_rename_pruductorder_productorder_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userorder',
            name='fullname',
            field=models.CharField(max_length=40, null=True, verbose_name='نام کامل'),
        ),
        migrations.AlterField(
            model_name='userorder',
            name='total_price',
            field=models.PositiveIntegerField(default=0, verbose_name='هزینه کل'),
        ),
    ]
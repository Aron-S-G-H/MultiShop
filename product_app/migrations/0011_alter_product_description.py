# Generated by Django 4.1.2 on 2023-02-23 16:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0010_alter_product_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
    ]

# Generated by Django 4.1.2 on 2023-03-04 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userModel_app', '0005_user_discount_usage_alter_user_is_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='discount_usage',
        ),
    ]

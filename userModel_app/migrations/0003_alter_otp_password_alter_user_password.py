# Generated by Django 4.1.3 on 2022-11-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userModel_app', '0002_alter_user_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='password',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=60, verbose_name='گذرواژه'),
        ),
    ]

# Generated by Django 4.1.2 on 2023-03-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0006_alter_sendemail_options_alter_sendemail_file_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sendemail',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='فایل'),
        ),
    ]

# Generated by Django 4.1.2 on 2023-03-01 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0007_alter_sendemail_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sendemail',
            options={'verbose_name': 'ارسال پیام به کاربر', 'verbose_name_plural': 'ارسال پیام به کاربران'},
        ),
        migrations.AlterField(
            model_name='sendemail',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='messages_file', verbose_name='فایل'),
        ),
        migrations.AlterField(
            model_name='sendemail',
            name='send_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='زمان ارسال'),
        ),
    ]

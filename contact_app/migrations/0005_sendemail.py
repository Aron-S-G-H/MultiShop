# Generated by Django 4.1.2 on 2023-03-01 16:32

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contact_app', '0004_alter_contactinfo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendEmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=50, verbose_name='')),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='')),
                ('file', models.FileField(upload_to='', verbose_name='')),
                ('send_at', models.DateTimeField(auto_now=True, verbose_name='')),
                ('submit_status', models.BooleanField(blank=True, verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': '',
            },
        ),
    ]
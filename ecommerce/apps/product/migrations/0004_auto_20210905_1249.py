# Generated by Django 3.2 on 2021-09-05 12:49

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20210905_1046'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo_large',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.apng', force_format=None, keep_meta=True, null=True, quality=0, size=[720, 720], upload_to='', verbose_name='image large'),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_small',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='default.apng', force_format=None, keep_meta=True, null=True, quality=0, size=[300, 300], upload_to='', verbose_name='image small'),
        ),
    ]

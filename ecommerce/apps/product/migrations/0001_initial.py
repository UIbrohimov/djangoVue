# Generated by Django 3.2 on 2021-09-05 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_resized.forms
import model_utils.fields
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('photo_large', django_resized.forms.ResizedImageField(crop=None, default='default.apng', force_format=None, keep_meta=True, null=True, quality=0, size=[720, 720], upload_to='', verbose_name='image large')),
                ('photo_small', django_resized.forms.ResizedImageField(crop=None, default='default.apng', force_format=None, keep_meta=True, null=True, quality=0, size=[300, 300], upload_to='', verbose_name='image small')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=100, verbose_name='name')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('specs', models.TextField(blank=True, verbose_name='Characteristics')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='slug')),
                ('id_number', models.CharField(blank=True, max_length=200, verbose_name='Identification number')),
                ('instruction_file', models.FileField(blank=True, help_text='optional', upload_to='product/')),
                ('price', models.DecimalField(decimal_places=2, help_text='price in USD($)', max_digits=10, verbose_name='price')),
                ('price_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='price_discount')),
                ('rating', models.IntegerField(blank=True, default=0, verbose_name='????????????')),
                ('available', models.BooleanField(default=True, verbose_name='available')),
                ('bestseller', models.BooleanField(default=False, verbose_name='bestseller')),
                ('discount', models.BooleanField(default=False, verbose_name='Stock')),
                ('deleted', models.BooleanField(default=False, verbose_name='Deleted')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proudcts', to='product.category')),
                ('publisher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]

from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import TimeStampedModel
from django.contrib.auth import get_user_model
from django.urls import reverse
from django_resized import ResizedImageField

from mptt.models import MPTTModel, TreeForeignKey


User = get_user_model()


class Category(MPTTModel, TimeStampedModel):
    title = models.CharField(_("Title"), max_length=255)
    slug = models.SlugField(_("Slug"), max_length=300, unique=True, blank=True)
    parent = TreeForeignKey(
        'self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')

    photo_large = ResizedImageField(
        _('image large'), size=[720, 720], default='default.apng', blank=True, null=True)
    photo_small = ResizedImageField(
        _('image small'), size=[300, 300], default='default.apng', blank=True, null=True)

    class MPTTMeta:
        order_insertsion_by = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:list_by_cat', kwargs={"slug": self.slug})

    def get_vue_url(self):
        return f"/{self.slug}/"


# Create your models here.
class Product(TimeStampedModel):

    publisher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, related_name='proudcts', blank=True, null=True)

    title = models.CharField(_('name'), max_length=100)

    slug = models.SlugField(_('slug'), max_length=200, unique=True)

    description = models.TextField(_("description"), blank=True)

    specs = models.TextField(_("Characteristics"), blank=True)

    id_number = models.CharField(_('Identification number'), blank=True, max_length=200)
    
    instruction_file = models.FileField(upload_to = 'product/', blank=True, help_text='optional')

    price = models.DecimalField(_('price'),help_text=_("price in USD($)"),max_digits=10, decimal_places=2)
    
    price_discount = models.DecimalField(_('price_discount'),
                                        max_digits=10, decimal_places=2, blank=True, null=True)
    
    rating = models.IntegerField("Оценка", blank=True, default=0)

    available = models.BooleanField(_('available'), default=True)
    
    bestseller = models.BooleanField(_('bestseller'), default=False)
    
    discount = models.BooleanField(_('Stock'), default=False)
    
    deleted = models.BooleanField(_("Deleted"), default=False)
    
    photo_large = ResizedImageField(
        _('image large'), quality=100, size=[720, 720], default='default.apng', blank=True, null=True)
    photo_small = ResizedImageField(
        _('image small'), quality=100, size=[300, 300], default='default.apng', blank=True, null=True)


    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('Products')
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={"slug": self.slug})

    def get_vue_url(self):
        return f"/{self.category.slug}/{self.slug}/"

    def get_large_image(self):
        return "http://127.0.0.1:8000" + self.photo_large.url
    
    def get_small_image(self):
        return "http://127.0.0.1:8000" + self.photo_small.url

    # def get_large_image(self):
    #     image = self.images.first()
    #     return image.get_url(large=True)
    
    # def get_small_image(self):
    #     image = self.images.first()
    #     return image.get_url(large=False)

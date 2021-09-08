from django.db import models
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField
from apps.product.models import Product

class Picture(models.Model):

    # product = models.ForeignKey(
    #     Product, on_delete=models.CASCADE, verbose_name=_("Продукт"),
    #     related_name='images', null=True, blank=True
    #     )

    photo_large = ResizedImageField(_('image large'), size=[720, 720], default='default.apng', blank=True, null=True)
    photo_small = ResizedImageField(_('image small'), size=[300, 300], default='default.apng', blank=True, null=True)

    class Meta:
        abstract = True

    def get_url(self, large=False):
        if large:
            return 'http://127.0.0.1:800' + self.photo_large.url
        return 'http://127.0.0.1:800' + self.photo_small.url

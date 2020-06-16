
# Create your models here.
from django.db import models
from django.urls import reverse

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utilities import unique_slug_generator
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique = True)
    description = models.TextField(max_length = 1000, blank = True, null = True)
    price = models.DecimalField(decimal_places = 2, max_digits = 10, default = 0.0)
    summary = models.TextField(max_length=200, default = "item summary")
    featured = models.BooleanField(default = True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    slug = models.CharField(max_length=60, default='qwerty')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return f"/product/{self.title}/"
        return reverse("main_product:product_detail", kwargs={"my_title":self.title})


@receiver(pre_save, sender = Product)
def pre_save_slug(sender,**kwargs):
    print(kwargs)
    slug = unique_slug_generator(kwargs["instance"])
    kwargs["instance"].slug = slug
from django.db import models
from django.urls import reverse

from django.db.models.signals import pre_save
from django.dispatch import receiver
from .utilities import unique_slug_generator
from django.conf import settings
# Create your models here.



class Contact(models.Model):
    name = models.CharField(max_length=15)
    position = models.CharField(max_length=50)
    joined = models.DateTimeField(auto_now_add=True)
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    summary = models.TextField(max_length=200, default="About yourself")
    current = models.BooleanField(default=True)
    email = models.CharField(max_length=25)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return f"/product/{self.title}/"
        return reverse("main_contact:contact_detail", kwargs={"my_name": self.name})

@receiver(pre_save, sender=Contact)
def pre_save_slug(sender, **kwargs):
    print(kwargs)
    slug = unique_slug_generator(kwargs["instance"])
    kwargs["instance"].slug = slug


from django.db import models

# Create your models here.

class Contact(models.Model):
    FullName = models.CharField(max_length=30, unique=True)
    contact = models.DecimalField(decimal_places = 0, max_digits=10, default =0)

    def __str__(self):
        return self.FullName
from django.db import models


# Create your models here.

class Employees(models.Model):
    name = models.CharField(max_length=20)
    position = models.CharField(max_length=15)
    dob = models.DateField()
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    email = models.CharField(max_length=25)
    contact = models.CharField(max_length=15)
    current = models.BooleanField(default=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

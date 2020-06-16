from django import forms
from .models import Product
from django.forms.utils import ValidationError

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = {
            "title",
            "description",
            "price",
            "summary",
        }

        def clean_title(self, *args, **kwargs):
            title = self.cleaned_data.get("title")
            if "JPT" in title:
                raise ValidationError("This is not a valid title for Product")
            else:
                return title

        def clean_summary(self,*args,**kwargs):
            summary = self.cleaned_data.get("summary")
            if len(summary)>200:
                raise ValidationError("Too lengthy to be called a summary.")
            if len(summary)<5:
                raise ValidationError("Too short for a validation")
            else:
                return summary

        def clean_price(self, *args, **kwargs):
            price = self.cleaned_data.get("price")
            if (price<0):
                raise ValidationError("Price cannot be negative")
            counter =0
            for i in str(price):
                if i == ".":
                    counter +=1
            if counter >1:
                raise ValidationError("Cannot have more than one decimal point. ")
            else:
                return price


from django import forms
from .models import Contact
from django.forms.utils import ValidationError

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = {
            "name",
            "summary",
            "salary",
        }

        def clean_name(self, *args, **kwargs):
            name = self.cleaned_data.get("name")
            if "JPT" in name:
                raise ValidationError("This is not a valid title.")
            else:
                return name

        def clean_summary(self,*args,**kwargs):
            summary = self.cleaned_data.get("summary")
            if len(summary)>200:
                raise ValidationError("Too lengthy to be called a summary.")
            if len(summary)<5:
                raise ValidationError("Too short for a validation")
            else:
                return summary

        def clean_salary(self, *args, **kwargs):
            salary = self.cleaned_data.get("salary")
            if (salary<0):
                raise ValidationError("Salary cannot be negative")
            counter =0
            for i in str(salary):
                if i == ".":
                    counter +=1
            if counter >1:
                raise ValidationError("Cannot have more than one decimal point. ")
            else:
                return salary


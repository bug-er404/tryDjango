from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm

# Create your views here.

def simple_function_view_render_default(request, *args, **kwargs):
    context = {"key":"This is a", "key2":"development site."}
    return render(request,"default.html", context)


def contact_list_function_view(request, *args, **kwargs):
    objects = Contact.objects.filter()
    context = {
        "objects":objects
    }
    print(objects)
    return render(request, "contact/contact_list.html",context)

def contact_create_function_view(request, *args, **kwargs):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    else:
        print(form.errors)

    context = {"form": form}
    return render(request,"contact/contact_create.html",context)

def contact_detail_function_view(request, *args, **kwargs):
    obj_data = Contact.objects.get(slug = my_slug)
    context = {
        "object":obj_data,

    }
    return render(request,"contact/contact_detail.html",context)

def contact_delete_function_view(request, *args, **kwargs):
    obj = get_object_or_404(Product, title = my_title)
    if request.method == "POST":
        obj.delete()
        return redirect("/contact/")
    context= {
        "object":obj
    }
    return render(request,"contact/contact_delete.html", context)



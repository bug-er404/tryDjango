from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product
from .forms import ProductForm

# Create your views here.

def simple_function_view_response(request, *args, **kwargs):
    print(request.user)
    print(args)
    print(kwargs)
    return HttpResponse("<h1> Hello World! </h1>")

def simple_function_view_render_default(request, *args, **kwargs):
    context = {"key":"this is value", "key2":1234657498}
    return render(request,"default1.html", context)

def contact_function_view(request, *args, **kwargs):
    return render(request,"Contact.html", {})

def product_detail_function_view(request, my_title, *args,**kwargs):
    obj_data = Product.objects.get(slug = my_slug)
    context = {
        "object":obj_data,

    }
    return render(request,"products/product_detail.html",context)

def product_create_function_view(request,*args,**kwargs):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            instance = form.save(commit=False)
            instance.seller = request.user
            instance.save()
        else:
            return HttpResponseRedirect("/admin/ ")
        print(form.cleaned_data)
        form = ProductForm()
    else:
        print(form.errors)

    context = {"form": form}
    return render(request,"products/product_create.html",context)

def product_list_function_view(request, *args, **kwargs):
    objects = Product.objects.filter(seller = request.user)
    context = {
        "objects":objects
    }
    print(objects)
    return render(request, "products/product_list.html",context)

def product_delete_function_view(request, my_title, *args, **kwargs):
    obj = get_object_or_404(Product, title = my_title)
    if request.method == "POST":
        obj.delete()
        return redirect("/product/")
    context= {
        "object":obj
    }
    return render(request,"products/product_delete.html", context)


def product_apiview_1():
    pass


def product_apiview_2():
    pass

def product_apiview_3():
    pass

def product_apiview_4():
    pass



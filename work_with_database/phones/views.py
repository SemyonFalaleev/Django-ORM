from django.shortcuts import render, redirect
from .models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    sort_key = request.GET.get('sort', 'name')
    if sort_key == "min_price":
        phones = Phone.objects.all().order_by('price')
    elif sort_key == 'max_price':
        phones = Phone.objects.all().order_by('-price')
    else:
        phones = Phone.objects.all().order_by(sort_key) 
    template = 'catalog.html'
    context = {"phones": phones,
               }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug).first()
    context = {
        "phone": phone,
    }
    return render(request, template, context)

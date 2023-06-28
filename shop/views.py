from django.shortcuts import get_object_or_404, render
from . models import *
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, InvalidPage

# Create your views here.

def home(request, c_slug = None):
    prodt = None
    if c_slug!=None:
        c_page=get_object_or_404(category, slug=c_slug)
        prodt = products.objects.all().filter(categories = c_page, available=True)
    else:
        prodt = products.objects.all().filter(available=True)
    cat = category.objects.all()
    paginator = Paginator(prodt, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'index.html',  {'prodt':prodt, 'cat':cat, 'pg': pro})


def catview(request, c_slug = None):
    c_page = None
    prodt = None

    if c_slug!=None:
        c_page=get_object_or_404(category, slug=c_slug)
        prodt = products.objects.filter(categories = c_page, available = True)
    
    else:
        prodt = products.objects.all().filter(available=True)
    cat = category.objects.all()
    paginator = Paginator(prodt, 8)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pro = paginator.page(page)
    except(EmptyPage, InvalidPage):
        pro = paginator.page(paginator.num_pages)
    return render(request, 'products.html', {'pr':prodt, 'cat':cat, 'pg': pro})



def prodetails(request, c_slug, product_slug):
    try:
        prod = products.objects.get(categories__slug = c_slug, slug = product_slug)

    except Exception as e:
        raise e
    return render(request, 'detail.html', {'pr':prod})

def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        cat = category.objects.all()
        prod = products.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request, 'search.html', {'qr':query, 'pr': prod,  'cat':cat})


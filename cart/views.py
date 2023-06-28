from django.shortcuts import render, redirect, get_object_or_404
from shop.models import *
from . models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User, auth

# Create your views here.

def cart_details(request, tot = 0, count = 0, ct_items = None, ship = 0):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.product.price*i.quantity)
            count += i.quantity
            ship += count*2
        gt = int(tot+ship)
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count, 'gt':gt, 'ship':ship})

def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

def add_cart(request, product_id):
    prod = products.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id = c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id = c_id(request))
        ct.save()
    try:
        c_items = items.objects.get(product = prod, cart = ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items = items.objects.create(product = prod, quantity = 1, cart = ct)
        c_items.save()
    return redirect('cartdetails')
    
    
def min_cart(request,product_id):
    ct = cartlist.objects.get(cart_id = c_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(product = prod, cart = ct)
    if c_items.quantity>1:
        c_items.quantity-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartdetails')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id = c_id(request))
    prod = get_object_or_404(products, id=product_id)
    c_items = items.objects.get(product = prod, cart = ct)
    c_items.delete()
    return redirect('cartdetails')

def checkout(request, tot = 0, count = 0, ct_items = None, ship = 0):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.product.price*i.quantity)
            count += i.quantity
            ship += count*2
        gt = int(tot+ship)
    except ObjectDoesNotExist:
        pass
    return render(request, 'checkout.html', {'ct': ct_items, 'tot': tot, 'cnt': count, 'gto':gt, 'shipp':ship})
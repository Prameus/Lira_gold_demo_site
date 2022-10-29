from django.shortcuts import render
from django.http import JsonResponse

import json

from authentication_management.views import reddirecting_page
from products.models import OrderItem, Product, Order


def home(request):
    product_list = Product.objects.all()

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
        customer=customer, complete=False)
    else:
        order = {'get_cart_total': 0, }

    context = {"product_list": product_list,'order':order}
    return render(request, 'home.html', context)


def search_page(request):
    searched = None
    print(request.method)
    if request.method == 'POST':
        searched = request.POST.get('searched')
        print(searched)
    print(searched)
    # if request.method == 'POST':
    #     print('aweaweaweawe')
    #     searched = request.POST['searched']

    #     return render(request, "search_page.html", {'searched': searched})
    # else:
    return render(request, "product_pages/search_page.html", {'searched': searched})


def profile(request, *args, **kwargs):
    if request.method == 'POST':
        if request.user.is_authenticated():
            return render(request, "authenticate_pages/profile.html", {})
        else:
            reddirecting_page(request)
            pass
    return render(request, "authenticate_pages/profile.html", {})


def cart(request):


    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0,}
    
    total = 0
    tax = 100
    for i in items: total += i.get_total
    subtotal = tax + total 

    context = {'items': items,'order':order, 'subtotal':subtotal}
    return render(request, ('product_pages/cart.html'), context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('productId:',productId)
    print('productId:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
 

# def earrings(request, *args, **kwargs):
#     earrings_list = Earrings.objects.all()
#     context = {'earrings_list': earrings_list}

#     return render(request, 'product_pages/earrings.html', context)


# def rings(request, *args, **kwargs):
#     rings_list = Ring.objects.all()
#     context = {'rings_list': rings_list}

#     return render(request, 'product_pages/rings.html', context)


# def bracelets(request, *args, **kwargs):
#     bracelets_list = Bracelet.objects.all()
#     context = {'bracelets_list': bracelets_list}

#     return render(request, 'product_pages/bracelets.html', context)


# def necklaces(request, *args, **kwargs):
#     necklaces_list = Necklace.objects.all()
#     context = {'necklaces_list': necklaces_list}

#     return render(request, 'product_pages/necklaces.html', context)

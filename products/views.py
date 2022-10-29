# from django.shortcuts import render

# from .models import *

# def home(request):
#     product_list = Product.objects.all()

#     context = {"product_list": product_list}
#     return render(request,'home.html',context)

# def search_page(request):
    
#     context = {}
#     return render(request, ('product_pages/search_page.html'),context)

# def cart(request):

#     if request.user.is_authenticated:
#         customer = request.user.customer
#         order, created = Order.objects.get_or_create(customer=customer, complete=False)
#         items = order.orderitem_set.all()
#     else:
#         items = []

#     context={'items':items}
#     return render(request, ('product_pages/cart.html'),context)
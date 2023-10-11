# views.py

from django.shortcuts import render
from django.views import View
from user.models import User, Cart, Address

class CartView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        cart = Cart.objects.get(user=user)
        return render(request, 'cart.html', {'user': user, 'cart': cart})

class AddressListView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        addresses = Address.objects.filter(user=user)
        return render(request, 'address_list.html', {'user': user, 'addresses': addresses})

    # 其他订单、支付、退货退款的视图函数声明
    # ...

# views.py

from django.shortcuts import render
from django.views import View
from products.models import Product


class ProductListView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request, 'product_detail.html', {'product': product})

    # 其他条件查询的视图函数声明
    # ...

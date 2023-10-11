# views.py

from django.shortcuts import render
from django.views import View
from data_analysis.models import Data


class DataListView(View):
    def get(self, request):
        data_list = Data.objects.all()
        return render(request, 'data_list.html', {'data_list': data_list})


class DataDetailView(View):
    def get(self, request, pk):
        data_object = Data.objects.get(pk=pk)
        return render(request, 'data_detail.html', {'data_object': data_object})

    # 其他数据分析和可视化的视图函数声明
    # ...

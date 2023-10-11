from django.urls import path
from . import views

urlpatterns = [
    path('data/', views.DataListView.as_view(), name='data_list'),
    path('data/<int:pk>/', views.DataDetailView.as_view(), name='data_detail'),
    # 其他数据分析和可视化的路由
]
from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>/cart/', views.CartView.as_view(), name='cart'),
    path('users/<int:user_id>/addresses/', views.AddressListView.as_view(), name='address_list'),
    # 其他订单、支付、退货退款的路由
]




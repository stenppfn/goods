from django.urls import path
from . import views

urlpatterns = [
    path('users/<int:user_id>/info/', views.UserInfoView.as_view(), name='user_info'),
    path('users/<int:user_id>/updates/', views.UpdatesView.as_view(), name='system_updates'),
    # 其他用户信息管理、密码找回、系统推送的路由
]
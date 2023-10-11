from django.urls import path
from . import views

urlpatterns = [
    path('consultations/', views.ConsultationListView.as_view(), name='consultation_list'),
    path('consultations/<int:pk>/', views.ConsultationDetailView.as_view(), name='consultation_detail'),
    # 其他客服管理的路由
]
# views.py

from django.shortcuts import render
from django.views import View
from consultations.models import Consultation


class ConsultationListView(View):
    def get(self, request):
        consultations = Consultation.objects.all()
        return render(request, 'consultation_list.html', {'consultations': consultations})


class ConsultationDetailView(View):
    def get(self, request, pk):
        consultation = Consultation.objects.get(pk=pk)
        return render(request, 'consultation_detail.html', {'consultation': consultation})

    # 其他客服管理的视图函数声明
    # ...

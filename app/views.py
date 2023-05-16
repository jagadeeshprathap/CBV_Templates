from typing import Any, Dict
from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse

class cbv_data(TemplateView):
    template_name='cbv_data.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        co=super().get_context_data(**kwargs)
        co['name']='mouni'
        co['age']=20
        return co
    

class cbv_formdata(TemplateView):
    template_name='cbv_formdata.html'
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        sfo=super().get_context_data(**kwargs)
        fo=studentform()
        sfo['fo']=fo
        return sfo
    

    def post(self,request):
        sfd=studentform(request.POST)
        if sfd.is_valid():
            sfd.save()
            return HttpResponse('data is inserted successfully')
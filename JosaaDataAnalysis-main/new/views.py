from typing import Any, Dict
from django.http import JsonResponse
from django.shortcuts import render
from .iits import posts
from django.views.generic import TemplateView
from .models import Admission
from django.core import serializers
from django.http import HttpResponse


context_iit={
        'posts':posts
    }

def home(request):
    return render(request,'new/home.html',context_iit)

def about(request):
    return render(request,'new/about.html',{'title':'About'})

def iitList(request):
    return render(request,'new/iitList.html',context_iit)

def iitb(request, college):
    data = Admission.objects.filter(institute=college)  # Filter data based on the college parameter
    serialized_data = serializers.serialize('json', data)
    context = {
        'data': serialized_data,
        'institute_name': college
    }
    return render(request, "new/iitb.html", context)

def insti_cutoff(request):
    # Get the distinct years
    years = Admission.objects.values('year').distinct()

    admissions_data = []
    for year in years:
        # Get the maximum round number for the current year
        max_round = (
            Admission.objects.filter(year=year['year'])
            .order_by('-round')
            .values('round')
            .first()
        )

        if max_round is not None:
            # Get the rows with the maximum round number for the current year
            rows = Admission.objects.filter(year=year['year'], round=max_round['round'])
            admissions_data.extend(rows)

    serialized_data = serializers.serialize('json', admissions_data)

    context = {
        'admissions_data': serialized_data,
    }

    return render(request, "new/insti_cutoff.html", context)





















# def iitb(request): 
#     data = Admission.objects.filter(institute='Indian Institute of Technology Bombay')  # Retrieve data for IIT Bombay
#     serialized_data = serializers.serialize('json', data)
#     context = {
#         'data': serialized_data
#     }
#     return render(request, "new/iitb.html", context)


# class AdmissionChartView(TemplateView):
#     template_name='new/iitb.html'
#     def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
#         context=super().get_context_data(**kwargs)
#         context["qs"]=Admission.objects.all()
#         return context
    
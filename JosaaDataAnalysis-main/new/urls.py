from django.urls import path
from . import views
from new.views import *

urlpatterns = [
    path('', views.home,name='josaa-home'),
    path('about/', views.about,name='josaa-about'),
    path('iitList/', views.iitList,name='iit-list'),
    # path('iitb/',views.iitb,name='iitb'),
    path('iitb/<str:college>/', views.iitb, name='iitb'),
    path('insti_cutoff/', views.insti_cutoff, name='insti_cutoff'),
    # path('iitb/',AdmissionChartView.as_view(),name='iitb'),
]

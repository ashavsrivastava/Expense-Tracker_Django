from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.analysis,name="analysis"),
    path('',views.analysis,name="predict"),

]
from django.contrib import admin
from django.urls import path
from . import views

app_name = "yapbitir"

urlpatterns = [
    path('yapbitirs/', views.yapbitirs, name="yapbitirs"),
    
]
"""
app_name = "yapbitir"


urlpatterns = [
    path('dashboard/', views.dashboard,name= "dashboard"),
    #path('yapbitirs/', views.yapbitirs,name= "yapbitirs"),
]


    path('addyapbitir/', views.addyapbitir,name= "addarticle"),
    path('yapbitir/<int:id>', views.detail,name= "detail"),
    path('update/<int:id>', views.updateYapbitir,name= "update"),
    path('delete/<int:id>', views.deleteYapbitir ,name= "delete"),
    path('', views.yapbitirss ,name= "yapbitirs"),
    path('comment/<int:id>', views.addComment ,name= "comment"),
    
"""


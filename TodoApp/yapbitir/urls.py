from django.contrib import admin
from django.urls import path
from . import views

app_name = "yapbitir"


urlpatterns = [
    path('dashboard/', views.dashboard,name= "dashboard"),
    #path('yapbitirs/', views.yapbitirs,name= "yapbitirs"),

    path('addyapbitir/', views.addyapbitir,name= "addyapbitir"),
    path('yapbitir/<int:id>', views.detail,name= "detail"),
    path('update/<int:id>', views.updateYapbitir,name= "update"),
    path('delete/<int:id>', views.deleteYapbitir ,name= "delete"),
    path('', views.yapbitirs ,name= "yapbitirs"),
    path('yes_finish/<int:id>', views.yes_finish,name="yes_finish"),
    path('no_finish/<int:id>', views.no_finish,name="no_finish"),
]

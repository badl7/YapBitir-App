from django.contrib import admin
from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('yapbitirs/', views.yapbitirs, name="yapbitirs"),
    
]
"""
app_name = "yapbitir"


urlpatterns = [
    path('dashboard/', views.dashboard,name= "dashboard"),
    #path('articles/', views.articles,name= "articles"),
]


    path('addarticle/', views.addarticle,name= "addarticle"),
    path('article/<int:id>', views.detail,name= "detail"),
    path('update/<int:id>', views.updateArticle ,name= "update"),
    path('delete/<int:id>', views.deleteArticle ,name= "delete"),
    path('', views.articles ,name= "articles"),
    path('comment/<int:id>', views.addComment ,name= "comment"),
    
"""


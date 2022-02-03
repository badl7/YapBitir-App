from django.contrib import admin

from .models import Yapbitir
# Register your models here.
@admin.register(Yapbitir)
class ListAdmin(admin.ModelAdmin):

    list_display = ["author","title","created_date","dateline"]
    
    list_display_links =["title","created_date"]
    
    search_fields = ["title"]

    list_filter = ["dateline"]

    class Meta:
        model = Yapbitir

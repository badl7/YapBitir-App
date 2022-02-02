from django.contrib import admin

from .models import List
# Register your models here.
@admin.register(List)
class ListAdmin(admin.ModelAdmin):

    list_display = ["author","title","created_date","dateline"]
    list_display_links =["title","created_date"]
    search_fields = ["title"]
    class Meta:
        model = List

from django.contrib import admin
from . import models
from django.db.models import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from django.contrib.admin import DateFieldListFilter

# Register your models here.


@admin.register(models.MetaData)
class Metadata(admin.ModelAdmin):
    list_display = ['SiteName','Laboratory_Name','Contact', 'data_count']

    @admin.display(ordering='SiteName')
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(data_count=Count('data'))
        return queryset

    def data_count(self, data):
        url = (
            reverse('admin:import_excel_db_data_changelist') 
            + '?'
            + f'Site={data.SiteName}'
            )
        return format_html('<a href="{}">{}</a>', url,data.data_count) # Not_working
    

@admin.register(models.Data)
class Data(admin.ModelAdmin):
    list_display = ['Sample_Name','Type_of_Rain_Collector','Date', 'Site']
    list_filter = ('Site',  'Type_of_Rain_Collector')

    date_hierarchy = 'Date'

    search_fields = ['Sample_Name__istartswith']
from django.contrib import admin
from . models import Todo
import csv
from django.http import HttpResponse
from django.contrib.admin import DateFieldListFilter
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

# Register your models here.

class DownloadCsv:
    def download_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    download_as_csv.short_description = "Download Selected"

class TodoListAdmin(admin.ModelAdmin,DownloadCsv):
	list_display = ("title", "description", "status", "task_date",)
	search_fields = ("title", "description","status",)
	actions = ("download_as_csv",)
	list_filter = ("status",("created_at", DateRangeFilter), ("task_date", DateTimeRangeFilter),)

admin.site.register(Todo,TodoListAdmin)

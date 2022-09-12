from django.contrib import admin
from .models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['owner', 'make', 'model',  'fuel', 'color', 'date_of_production']
    list_filter = ['make', 'model',  'fuel']

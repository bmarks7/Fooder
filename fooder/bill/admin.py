from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import FoodItem, Food

admin.site.register(FoodItem)
admin.site.register(Food)
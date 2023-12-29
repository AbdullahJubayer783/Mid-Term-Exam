from django.contrib import admin
from . import models

# Register your models here.
# admin.site.register(models.brands)
class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display =['name', 'slug']
admin.site.register(models.brands, BrandAdmin)
from django.contrib import admin
from . models import *

# Register your models here.

class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(category, catadmin)


class prodadmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products, prodadmin)


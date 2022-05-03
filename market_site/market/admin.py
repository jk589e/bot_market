from django.contrib import admin

# Register your models here.
from .models import Items

#admin.site.register(Items)
@admin.register(Items)
class customeritems(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "discount")
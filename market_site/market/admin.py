from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportMixin
# Register your models here.
from .models import Items, User, TelegramLog

#admin.site.register(Items)
@admin.register(Items)
class marketItems(ImportExportMixin, admin.ModelAdmin):
    def photo1(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    photo1.short_description = 'Image'
    list_display = ("image_preview", "id", "name", "description", "price", "discount")
    search_fields = ['article', 'name',]

@admin.register(User)
class marketUsers(admin.ModelAdmin):
    list_display = ("id", "user_id", "user_name", "first_name", "last_name", "email", "phone_number", "status")

@admin.register(TelegramLog)
class marketLogs(admin.ModelAdmin):
    list_display = ("id", "message_text", "message_date" ,"message_from_id", "user_name", "first_name", "last_name")
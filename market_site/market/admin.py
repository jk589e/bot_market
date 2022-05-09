from django.contrib import admin

# Register your models here.
from .models import Items, User, TelegramLog

#admin.site.register(Items)
@admin.register(Items)
class marketItems(admin.ModelAdmin):
    list_display = ("id", "name", "description", "price", "discount")

@admin.register(User)
class marketUsers(admin.ModelAdmin):
    list_display = ("id", "user_id", "user_name", "first_name", "last_name", "email", "phone_number", "status")

@admin.register(TelegramLog)
class marketLogs(admin.ModelAdmin):
    list_display = ("id", "message_text", "message_date" ,"message_from_id", "user_name", "first_name", "last_name")
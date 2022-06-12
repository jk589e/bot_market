from django.contrib import admin
from django.utils.html import format_html
from import_export.admin import ImportExportMixin
from django.contrib.auth.models import User as use
# Register your models here.
from django.contrib.sessions.models import Session
from .models import Items, User as us, TelegramLog, Basket, BasketPosition
import pprint
#admin.site.register(Items)
@admin.register(Items)
class marketItems(ImportExportMixin, admin.ModelAdmin):
    def photo1(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    photo1.short_description = 'Image'
    list_display = ("image_preview", "id", "name", "description", "price", "discount")
    list_filter = ['price']
    search_fields = ['article', 'name']


@admin.register(us)
class marketUsers(ImportExportMixin, admin.ModelAdmin):
    def user_photo(self, obj):
        return format_html('<img src="{}" />'.format(obj.image.url))

    user_photo.short_description = 'Image'
    list_display = ("id", "photo_preview" ,"user_id", "user_name", "first_name", "last_name", "email", "phone_number", "status")
    search_fields = ['user_id', 'user_name', 'first_name','last_name', 'email','phone_number']

    def get_search_results(self, request, queryset, search_term):
        print("In get search results")
        results = super().get_search_results(request, queryset, search_term)
        return results
    list_filter = ['user_id', 'user_name']
@admin.register(TelegramLog)
class marketLogs(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "message_text", "message_date" ,"message_from_id", "user_name", "first_name", "last_name")
    list_filter = ['message_from_id', 'user_name']
#@admin.register(Basket)
class Basket(ImportExportMixin, admin.ModelAdmin):
    list_display = ("id", "user", "qty", "amount", "discount", "created_date")
    list_filter = ['user','created_date']

@admin.register(BasketPosition)
class BasketPosition(ImportExportMixin, admin.ModelAdmin):
    list_display = ("user", "item", "qty", "amount", "discount", "date_add")
    #list_filter = ['item', 'date_add']
    search_fields = ['item']



@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    def user(self, obj):
        session_user = obj.get_decoded().get('_auth_user_id')
        user = use.objects.get(pk=session_user)
        return user.username
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags = True
    list_display = ['user', 'session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
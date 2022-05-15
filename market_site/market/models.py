from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class Items(models.Model):
    article = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    vat = models.DecimalField(max_digits=15, decimal_places=2)
    discount = models.DecimalField(max_digits=15, decimal_places=2,null=True, blank=True)
    photo1 = models.ImageField(upload_to='images/', null=True, blank= True)

    def __str__(self):
        return self.name

    def image_preview(self):
        if self.photo1:
            return mark_safe('<img src="{0}" width="150" height="150" />'.format(self.photo1.url))
        else:
            return '(No image)'

class User(models.Model):
    user_id = models.BigIntegerField()
    user_name = models.CharField(max_length=100, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    first_message_time = models.DateTimeField(auto_now=True,blank=True)
    last_active_time = models.DateTimeField(null=True, blank=True)
    status = models.IntegerField(null=True,blank=True)

    def __str__(self):
        if self.user_name == None:
            res = str(self.user_id)
        else:
            res = self.user_name
        return (res)

class TelegramLog(models.Model):
    update_id = models.BigIntegerField()
    message_id = models.BigIntegerField(null=True)
    message_from_id = models.BigIntegerField()
    message_chat_id = models.BigIntegerField(null=True)
    inlinequery_id = models.BigIntegerField(null=True)
    callbackquery_id = models.BigIntegerField(null=True)
    user_name = models.CharField(max_length=100, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    message_text = models.CharField(max_length=2000, null=True)
    message_date = models.DateTimeField(auto_now=True)
    latitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    longitude = models.DecimalField(max_digits=12, decimal_places=8, null=True)
    processed = models.IntegerField(null=True)






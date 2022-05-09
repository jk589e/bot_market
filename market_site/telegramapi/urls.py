from django.urls import path

from . import views


urlpatterns = [
    path('5353508249:AAEwYhk4JJVKgKxRAlsthZtmwdE26BrpJ-c/', views.UpdateBot.as_view(), name='update'),
]
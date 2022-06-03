from django.urls import path

from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('testform/',views.test_form, name='testform'),
    path('testform/save/', views.test, name='test'),
]

from django.urls import path

from . import views



urlpatterns = [

    path('', views.index, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('basket/save/', views.saveBasket, name='test'),
    path('basket/getHeaders/', views.getBasketHeaders, name='basketheaders'),
    path('larisagift20220722/', views.gift, name='gift'),
    path('basket/<int:usert_id>/', views.getBasket, name='basket'),
    path('larisagift20220722/download/', views.giftDownload, name='giftDownload'),
    path('larisagift20220722/music/', views.giftMusic, name='giftMusic'),
]

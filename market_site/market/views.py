from django.http import HttpResponse
from .models import Items, Formtest, BasketPosition, User
from django.template import loader
from django.http import Http404
from django.shortcuts import render
from django.db.models import Avg, Count, Sum

from .telegram_api import  send_message

from django.http import JsonResponse

def index(request):
    latest_objects = Items.objects.all()
    template = loader.get_template('market/index_20220704.html')
    context = {
        'latest_objects': latest_objects,
    }
    #output = ', '.join([q.name for q in latest_objects])
    return HttpResponse(template.render(context, request))

def detail(request, item_id):
    try:
        item = Items.objects.get(pk=item_id)
    except Items.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'market/detail1.html', {'item': item})


def saveBasket(request):
    if request.method == 'POST':

        #print(request.POST)
        item_id = request.POST.get('item')
        user_id = request.POST.get('user')
        if user_id == None:
            user_id = 5159671328

        item = Items.objects.get(pk=item_id)
        user = User.objects.get(user_id = user_id)
        basket = BasketPosition(item_id = item_id, user_id = user.id, qty= 1, amount = item.price + item.discount,
                                discount= item.discount, vat= item.vat, position= 1, basket_id = 1)



        basket.save()
        return render(request, 'market/testform.html')

def getBasketHeaders(request):
    if request.method == 'GET':
        user_id = request.GET.get('user')
        #user_id = 526697170
        user = User.objects.get(user_id=user_id)
        #basket = BasketPosition.objects.get(user_id=user.id)
        summ = BasketPosition.objects.filter(user_id=user).aggregate(summ=Sum('amount'))
        result = {'code': 200, "content": summ }
        print(summ)
        return JsonResponse(result)

def gift(request):

    template = loader.get_template('market/gift.html')

    #output = ', '.join([q.name for q in latest_objects])
    send_message(chat_id=526697170,message='коробка открыта')
    return render(request, 'market/gift.html')


#scp -rp /Users/jk58e9/Downloads/DashboardTest-31.05.2022.pdf jk58e9@app.unicbot.ru:/home/jk58e9/bot_market/bot_market/market_site/media/userphotos


def getBasket(request, usert_id):
   user_id = User.objects.get(user_id=usert_id)
   print(usert_id)
   print(user_id.id)
   basket_positions = BasketPosition.objects.filter(user_id=user_id.id).order_by('date_add')
   template = loader.get_template('market/basket.html')
   context = {
       'basket': basket_positions,
   }
   # output = ', '.join([q.name for q in latest_objects])
   return HttpResponse(template.render(context, request))

def giftDownload(request):
    if request.method == 'GET':
        send_message(chat_id=526697170, message='подарок открыт')
        result = {'code': 200, 'result': 'ok'}
        return JsonResponse(result)

def giftMusic(request):
    if request.method == 'GET':
        send_message(chat_id=526697170, message='песня открыта')
        result = {'code': 200, 'result': 'ok'}
        return JsonResponse(result)






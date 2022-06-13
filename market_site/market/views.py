from django.http import HttpResponse
from .models import Items, Formtest, BasketPosition, User
from django.template import loader
from django.http import Http404
from django.shortcuts import render

def index(request):
    latest_objects = Items.objects.all()
    template = loader.get_template('market/index_20220612.html')
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

        print(request.POST)
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






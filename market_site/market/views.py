from django.http import HttpResponse
from .models import Items
from django.template import loader
from django.http import Http404
from django.shortcuts import render

def index(request):
    latest_objects = Items.objects.all()
    template = loader.get_template('market/index.html')
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
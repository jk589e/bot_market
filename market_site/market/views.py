from django.http import HttpResponse
from .models import Items, Formtest
from django.template import loader
from django.http import Http404
from django.shortcuts import render

def index(request):
    latest_objects = Items.objects.all()
    template = loader.get_template('market/index_202206.html')
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


def test(request):
    if request.method == 'POST':
        #item= Items.objects.get(pk=2188)
        text = request.POST.get('testtext')
        t = Formtest(test = text)
        t.save()
        return render(request, 'market/testform.html')


def test_form(request):
    return render(request, 'market/testform.html')



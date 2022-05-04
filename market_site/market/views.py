from django.http import HttpResponse
from .models import Items
from django.template import loader

def index(request):
    latest_objects = Items.objects.all()
    template = loader.get_template('market/index.html')
    context = {
        'latest_objects': latest_objects,
    }
    #output = ', '.join([q.name for q in latest_objects])
    return HttpResponse(template.render(context, request))
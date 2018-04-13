from django.shortcuts import render
from django.http import HttpResponse

from .models import Application

# Create your views here.
def index(request):
    apps = Application.objects.all()


    col_av = []
    col_un = []
    context = {
        'apps':apps,
        'col_av':col_av,
        'col_un':col_un
    }

    for app in apps:
        if app.app_stat == 'av':
            col_av.append(app)
        elif app.app_stat == 'un':
            col_un.append(app)

    return render(request, 'index.html', context)

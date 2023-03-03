from django.http import HttpResponse
from django.shortcuts import render
from . import views
from appnoa.models import Contactform
# Create your views here.


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def contact(request):

    m = ''
    if request.method == 'POST':
        myname = request.POST.get('myname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        bio = request.POST.get('bio')
        images = request.POST.get('images')
        data = Contactform(myname=myname, email=email,
                       password=password, bio=bio, images=images)
        data.save()
        m = 'your data has been sent sir you can go and check Here Is The Link'
    return render(request, 'contact.html', {'m': m})


def services(request):
    return render(request, 'services.html')

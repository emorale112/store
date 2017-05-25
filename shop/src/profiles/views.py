from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    template = 'home.html'
    return render(request, template, context)

def wino(request):
    context = {}
    template = 'wino.html'
    return render(request, template, context)

def featured(request):
    context = {}
    template = 'featured.html'
    return render(request, template, context)

def shop(request):
    context = {}
    template = 'shop.html'
    return render(request, template, context)


@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request, template, context)

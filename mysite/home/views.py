from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'personal/home.html')

def about_me(request):
    return render(request, 'personal/about_me.html')

def skills(request):
    return render(request, 'personal/skills.html')

def contactme(request):
    return render(request, 'personal/contactme.html')

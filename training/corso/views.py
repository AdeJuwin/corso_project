from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    
    return render(request, 'corso/home.html')

def article(request):
    return render(request, 'corso/article-details.html', {'title': 'article-details'})

def privacy(request):
    return render(request, 'corso/privacy-policy.html', {'title': 'privacy-policy'})


def conditions(request):
    return render(request, 'corso/terms-conditions.html', {'title': 'terms-conditions'})
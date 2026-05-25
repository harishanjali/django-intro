from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
    return HttpResponse('<h1 style="font-family:sans-serif;text-align:center;">Hello World</h1>')

def info(request):
    return HttpResponse('<h1 style="font-family:sans-serif;">Hello Harish,LEts start Django</h1>')
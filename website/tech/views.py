from django.shortcuts import render

from django.http  import HttpResponse

def courses(request):
    return  HttpResponse("<h1>This is my homepage</h1>")

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista(request):
    return HttpResponse("Primer Texto")

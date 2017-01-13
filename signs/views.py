from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from .models import Screen

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ScreensAll(request):
    screens = Screen.objects.all().order_by('name')
    context = {'screens': screens}
    return render_to_response('screensall.html', context)

def SpecificScreen(request, screenslug):
    screen = Screen.objects.get(slug=screenslug)
    context = {'screen': screen}
    return render_to_response('singlescreen.html', context)


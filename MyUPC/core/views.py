from django.shortcuts import render, get_object_or_404

from django.http import Http404, HttpRequest, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, "index.html")

def todo(request):
    return render(request, "todo.html")

def grades(request):
    return render(request, "grades.html")

def nextstep(request):
    return render(request, "nextstep.html")

def us(request):
    return render(request, "aboutus.html")

def dia(request):
    return render(request, "dia.html")


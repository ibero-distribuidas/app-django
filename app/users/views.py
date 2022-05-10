from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hola mundo!")

def la_dos(request):
    return HttpResponse("Hola mundo 2!")
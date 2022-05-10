from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

# Create your views here.
def index(request):
    context = {'segment': 'index'}
    return render(request, 'home/index.html', context)


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        context = {'segment': 'index'}
        return render(request, 'home/index.html', context)
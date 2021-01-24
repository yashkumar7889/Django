from django.shortcuts import render, HttpResponse                              
from .models import Destination
# Create your views here.
def index(request):
    dests=Destination.objects.all()
    dests1=Destination.objects.all()
    return render(request, 'index.html', {'dests':dests, 'dests1':dests1})
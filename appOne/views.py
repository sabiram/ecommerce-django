from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    name = "sabira"
    job = "engineer"
    context = {"name": name, "job": job}
    return render(request, 'home.html', context)

from django.shortcuts import render
import pickle


# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def result(request):
    
    return render(request, 'home/result.html', {'result':x})

def model(request):
    return render(request, 'home/model.html')

def base(request):
    return render(request, 'home/base.html')

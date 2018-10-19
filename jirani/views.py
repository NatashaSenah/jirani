from django.shortcuts import render,redirect
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'jirani.html')
def jirani(request):
    return render(request,'all-jirani/jirani.html')
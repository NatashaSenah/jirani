from .forms import NewNeighbourhoodForm,BusinessForm
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Neighbourhood
# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    neighbours = Neighbourhood.objects.all()
    return render(request, 'jirani.html',locals())
@login_required(login_url='/accounts/login/')
def jirani(request):
    neighbours = Neighbourhood.objects.all()
    
    return render(request,'jirani.html',locals())
def search_results(request):

    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbourhood = Neighbourhood.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-jirani/search.html',{"message":message,"neighbourhood": searched_neighbourhood})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-jirani/search.html',{"message":message})
@login_required(login_url='/accounts/login/')
def new_neighbourhood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            # print('edrftgyhunjmik,lp.;')

            neighbourhood = form.save(commit=False)
            neighbourhood.save()
        return redirect('home')


    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})
@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            # print('edrftgyhunjmik,lp.;')

            business = form.save(commit=False)
            business.save()
        return redirect('home')


    else:
        form = BusinessForm()
    return render(request, 'business.html', {"form": form})
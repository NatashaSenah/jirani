from .forms import NewNeighbourhoodForm
from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'jirani.html')
@login_required(login_url='/accounts/login/')
def jirani(request):
    return render(request,'jirani.html')
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
            neighbourhood = form.save(commit=False)
            neighbourhood.editor = current_user
            neighbourhood.save()
        return redirect('home')

    else:
        form = NewNeighbourhoodForm()
    return render(request, 'new_neighbourhood.html', {"form": form})
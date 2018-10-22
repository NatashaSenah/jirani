from django.shortcuts import render,redirect
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'jirani.html')
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
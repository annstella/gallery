from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Image
# import datetime as dt

# Create your views here.
def welcome(request):
   return render(request, 'all-pics/today-pics.html')

def pics(request):
   pics = Image.objects.all()

   return render(request, 'all-pics/today-pics.html', {"pics":pics})

def search_results(request):
  
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html',{"message":message})

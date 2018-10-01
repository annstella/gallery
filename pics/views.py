from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from .models import Image, Category
# import datetime as dt

# Create your views here.
def welcome(request):
   return render(request, 'all-pics/today-pics.html')

def pics(request):
   pics = Image.objects.all()

   return render(request, 'all-pics/today-pics.html', {"pics":pics})

def search_results(request):
  
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_categories = Image.search_image(category)
        message = f"{category}"

        return render(request, 'all-pics/search.html',{"message":message,"images": searched_categories})

    else:
        message = " Found 0 images for the search term"
        return render(request, 'all-pics/search.html',{"message":message})

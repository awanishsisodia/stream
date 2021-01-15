from django.shortcuts import render,get_object_or_404
from app import models

# Create your views here.

def home(request):
    video_data= models.VideoData.objects.all()
    trend = models.Trending.objects.all()
    recent = models.Recently.objects.all()

    return render(request,"app/index.html",{"video":video_data,"trend":trend,"recent":recent})

def details(request):

    return render(request,"app/details.html")

def trending(request):
    logo=models.Logo.objects.all()
    return render(request,"app/trending.html",{"logo":logo})



def search_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    product=models.VideoData.objects.all().filter(name__icontains=query)
    if 'product_ids' in request.COOKIES:
        product_ids = request.COOKIES['product_ids']
        counter=product_ids.split('|')
        product_count_in_cart=len(set(counter))
    else:
        product_count_in_cart=0

    # word variable will be shown in html when user click on search button
    word="Searched Result :"
    return render(request,'app/index.html',{'products':products,'word':word})

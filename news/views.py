from django.shortcuts import render
from requests import request
from .models import  *
from django.views.generic import ListView
# Create your views here.

def home(request):
    latest_new = New.objects.filter().order_by('-id')[0:1]
    other_news = New.objects.filter().order_by('-id')[1:12]
    categories = Category.objects.all()
    regions = Region.objects.all()
    context = {
        'latest_new':latest_new,
        'other_news':other_news,
        'categories':categories,
        'regions':regions,


    }

    return render(request, 'home.html')


def detail(request,id):
    news = New.objects.get(id=id)
    category = Category.objects.get(id=news.category.id)
    rel_news = New.objects.filter(category=category).exclude(id=id)

    lugat ={
        'news':news,
        'category':category,
        'rel_news':rel_news,
    }
    return render(request, 'detail.html',lugat)

class AllNews(ListView):
    model = New
    template_name = 'all-news.html'

def category(request):
    category = Category.objects.get(id=id)
    news = New.objects.filter(category=category)

    return render(request,'category-news.html',{
        "category": category,
        "news" : news
    })

def region(request):
    region = Region.objects.get(id=id)
    news = New.objects.filter(region=region)

    return render(request,'region-news.html',{
        "region": region,
        "news" : news
    })
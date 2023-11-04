import datetime
from django.shortcuts import render
from datetime import datetime
from datetime import date
from .models import *

# Create your views here.

def index(request) : 
    return render(request, 'index.html')


def show_current_affairs(request) : 
    today = date.today()
    records_for_today = Article.objects.filter(date=today)
    unique_dates = (
    Article.objects
    .values('date')
        .exclude(date=today)  # Exclude the specific date
        .distinct()
        .order_by('date')  # Sort the dates in ascending order
    )
    context = {
        'date' : today,
        'current' : records_for_today,
        'previous' : unique_dates     
    }
    return render(request, "currentAffairs.html", context)


def show_single_article(request, id):
    query_set = Article.objects.get(id=id)
    
    context = {
        'query' : query_set
    }

    return render(request, 'show_article.html', context)



def show_previous_articles(request, date):
    formatted_date = datetime.strptime(date, "%b. %d, %Y").strftime("%Y-%m-%d")

    objects = Article.objects.filter(date=formatted_date)

    unique_dates = (
    Article.objects
    .values('date')
        .exclude(date=formatted_date) 
        .distinct()
        .order_by('date')  
    )
    print(unique_dates)

    context = {
        'date' : date,
        'objects' : objects,
        'other' : unique_dates
    }
    return render(request, 'show_previous.html', context)

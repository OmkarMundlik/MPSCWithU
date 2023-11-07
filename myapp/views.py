import datetime
from django.shortcuts import render, redirect
from datetime import datetime
from datetime import date
from .models import *
from .forms import TestForm, QuestionFormSet
import json


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
    tests = Test.objects.values('subject').distinct()
    context = {
        'date' : today,
        'current' : records_for_today,
        'previous' : unique_dates ,
        'tests' : tests
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


def create_test(request):
    if request.method == 'POST':
        test_form = TestForm(request.POST)
        question_formset = QuestionFormSet(request.POST, prefix='questions')

        if test_form.is_valid() and question_formset.is_valid():
            test = test_form.save()
            for form in question_formset:
                question = form.save(commit=False)
                question.test = test
                question.save()

            return redirect('/show_current_affairs')  # Redirect to the test list view

    else:
        test_form = TestForm()
        question_formset = QuestionFormSet(prefix='questions')

    return render(request, 'create_test.html', {'test_form': test_form, 'question_formset': question_formset})


def test_list(request, subject) :
    tests = Test.objects.filter(subject=subject)

    context = {'tests' : tests}
    return render(request, 'test_list.html', context)

def take_test(request, id):
    test = Test.objects.get(id=id)
    # Use the related name (assuming it's called 'question_set') to access the questions related to the test
    questions = Question.objects.filter(test=test)

    questions_list = list(questions.values('description', 'option_a', 'option_b', 'option_c', 'option_d', 'correct_option', 'answer_description'))

    # Convert the list to a JSON-serializable format
    questions_json = json.dumps(questions_list)

    
    print(questions_json)
    context = {'questions' : questions_json}
    return render(request, 'test.html', context)

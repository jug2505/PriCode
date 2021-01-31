from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Question, Choice


def home_page(request):    
    maxlen = 40 # Длина обрезанной статьи
    num_of_articles = 10 # Кол-во статей на странице

    article_titles = []
    article_texts = []
    
    # Возвращает последние 10 статей
    for item in Article.objects.all().order_by('-id')[:10]:
        article_titles.append(item.article_title)
        if (len(item.article_text) > maxlen):
            article_texts.append(item.article_text[:maxlen])
        else:
            article_texts.append(item.article_text)

    return render(
        request, 'courses/home.html', 
        {'article_titles': article_titles, 'article_texts': article_texts})

def courses(request, course_id):
    pass

from django.shortcuts import render
from django.http import HttpResponse

from .models import Article, Question, Choice


def home_page(request):    
    maxlen = 40 # Длина обрезанной статьи
    num_of_articles = 10 # Кол-во статей на странице

    article_titles = []
    article_texts = []
    article_ids = []
    
    # Возвращает последние 10 статей
    for item in Article.objects.all().order_by('-id')[:10]:
        article_titles.append(item.article_title)
        article_ids.append(item.id)
        if (len(item.article_text) > maxlen):
            article_texts.append(item.article_text[:maxlen])
        else:
            article_texts.append(item.article_text)

    return render(
        request, 'courses/home.html', {
            'article_titles': article_titles,
            'article_texts': article_texts,
            'article_ids': article_ids
            })

def article_add(request):
    if request.method == 'POST':
        # TODO: Создание объектов. Нужны id с фронта
        return redirect('courses/home.html')

    return render(request, 'courses/article_add.html')

def articles(request, course_id):
    pass

from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Article, Question, Choice


class HomeData:
    def __init__(self, article_text, article_title, article_id):
        self.article_title = article_title
        self.article_text = article_title
        self.article_id = article_id


def home_page(request):    
    maxlen = 40 # Длина обрезанной статьи
    num_of_articles = 3 # Кол-во статей на странице

    data = []
    
    # Возвращает последние 3 статьи
    for item in Article.objects.all().order_by('-id')[:num_of_articles]:
        if (len(item.article_text) > maxlen):
            data.append(HomeData(
                article_title=item.article_title, 
                article_text=item.article_text[:maxlen], 
                article_id=item.id))
        else:
            data.append(HomeData(
                article_title=item.article_title, 
                article_text=item.article_text, 
                article_id=item.id))

    return render(request, 'courses/home.html', {'articles': data})


def article_add(request):
    if request.method != 'POST':
        return render(request, 'courses/article_add.html')
    
    article = Article.objects.create(
        article_title=request.POST['article_title'], 
        article_text=request.POST['article_text'])

    question1 = Question.objects.create(
        article=article,
        question_text=request.POST['question1_text'])
    
    question2 = Question.objects.create(
        article=article,
        question_text=request.POST['question2_text'])

    question3 = Question.objects.create(
        article=article,
        question_text=request.POST['question3_text'])

    for i in range(1, 5, 1):
        Choice.objects.create(
            question=question1,
            choice_text=request.POST['q1_choice'+ str(i) + '_text'],
            choise_isRight=request.POST['blankRadio1']==str(i))
    
    for i in range(1, 5, 1):
        Choice.objects.create(
            question=question2,
            choice_text=request.POST['q2_choice'+ str(i) + '_text'],
            choise_isRight=request.POST['blankRadio2']==str(i))

    for i in range(1, 5, 1):
        Choice.objects.create(
            question=question3,
            choice_text=request.POST['q3_choice'+ str(i) + '_text'],
            choise_isRight=request.POST['blankRadio3']==str(i))
    
    return redirect('home')

    
def articles(request, course_id):
    pass


def catalog(request):

    article_titles = []
    article_texts = []
    article_ids = []

    for item in Article.objects.all().order_by('-id'):
        article_titles.append(item.article_title)
        article_ids.append(item.id)

    return render(
        request, 'courses/catalog.html', {
            'article_titles': article_titles,
            'article_texts': article_texts,
            'article_ids': article_ids
        })
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Article, Question, Choice


class HomeData:
    def __init__(self, article_text, article_title, article_id):
        self.article_title = article_title
        self.article_text = article_text
        self.article_id = article_id


class ChoiceData:
    def __init__(self, choice_text, choise_isRight):
        self.choice_text = choice_text
        self.choise_isRight = choise_isRight


class QuestionData:
    def __init__(self, question_text, choices):
        self.question_text = question_text
        self.choices = choices


class ArticleData:
    def __init__(self, questions, article_text, article_title, article_id):
        self.questions = questions
        self.article_title = article_title
        self.article_text = article_text
        self.article_id = article_id


def home_page(request):
    maxlen = 40  # Длина обрезанной статьи
    num_of_articles = 3  # Кол-во статей на странице

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
            choice_text=request.POST['q1_choice' + str(i) + '_text'],
            choise_isRight=request.POST['blankRadio1'] == str(i))

    for i in range(1, 5, 1):
        Choice.objects.create(
            question=question2,
            choice_text=request.POST['q2_choice' + str(i) + '_text'],
            choise_isRight=request.POST['blankRadio2'] == str(i))

    for i in range(1, 5, 1):
        Choice.objects.create(
            question=question3,
            choice_text=request.POST['q3_choice' + str(i) + '_text'],
            choise_isRight=request.POST['blankRadio3'] == str(i))

    return redirect('home')


def catalog(request):

    maxlen = 40  # Длина обрезанной статьи
    data = []

    for item in Article.objects.all().order_by('-id'):
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

    return render(request, 'courses/catalog.html', {'articles': data})


def show_article(request, article_id):
    info = Article.objects.get(id=article_id)
    article_title = info.article_title
    article_text = info.article_text
    questions_data = []
    info_question = Question.objects.all().filter(article=info)

    for question in info_question:
        questions_text.append(question.question_text)
        choices = Choice.objects.all().filter(question=question)
        choices_data = []
        for choice in choices:
            choices_data.append(ChoiceData(
                choice_text=choice.choice_text, choise_isRight=choice.choise_isRight))
        
        questions_data.append(QuestionData(question_text=question.question_text, choices=choices_data))

    data = ArticleData(
        article_id=article_id,
        article_text=article_text,
        article_title=article_title,
        questions=questions_data,)

    return render(request, 'courses/show_article.html', {'article': data})

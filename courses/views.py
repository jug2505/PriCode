from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Article, Question, Choice


class HomeData:
    def __init__(self, article_text, article_title, article_id):
        self.article_title = article_title
        self.article_text = article_text
        self.article_id = article_id


class ChoiceData:
    def __init__(self, choice_id, choice_text, choise_isRight):
        self.choice_id = choice_id # для идентификации конкретного ответа и его сравнения
        self.choice_text = choice_text
        self.choise_isRight = choise_isRight


class QuestionData:
    def __init__(self, question_id, question_text, choices):
        self.question_id = question_id # для идентификации группы радиокнопок
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
        choices = Choice.objects.all().filter(question=question)
        choices_data = []
        for choice in choices:
            choices_data.append(ChoiceData(
                choice_id=choice.id, choice_text=choice.choice_text, choise_isRight=choice.choise_isRight))

        questions_data.append(QuestionData(
            question_id=question.id, question_text=question.question_text, choices=choices_data))

    data = ArticleData(
        article_id=article_id, # содержит айди статьи, которая будет просматриваться
        article_text=article_text, # текст этой статьи
        article_title=article_title, # название статьи
        questions=questions_data,) # вопросы к статье. Вопросы содержат список вариантов ответа

    # проверка результатов
    if request.POST: # если был получен POST запрос, то начинаем обрабатывать
        answers = dict(request.POST) # создаю копию, потому что запрос не может быть изменен
        answers.pop('csrfmiddlewaretoken') # удаляю из словаря csrf токен чтоб не мешался
        for key, value in answers.items(): # key - question_id
            q = Choice.objects.all().filter(id=value[0]) # находим вариант ответа
            answers[key] = q[0].choise_isRight # заменяем id ответа на True | False
        
        # answers имеет структуру 'номер вопроса': bool
        right_percent = sum(value == True for value in answers.values()) / len(answers) # число от 0 до 1
        print(f"{right_percent: .0%}") # выводит в консоль процент правильных ответов
        
        # TODO: вывести результат на саму страницу
    
    return render(request, 'courses/show_article.html', {'article': data})

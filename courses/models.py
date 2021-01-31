from django.db import models


class Article(models.Model):
    article_title = models.TextField(default='')
    article_text = models.TextField(default='')


class Question(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    question_text = models.TextField(default='')


class Choice(model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    choise_isRight = models.BooleanField(default=False)

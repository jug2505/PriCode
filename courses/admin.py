from django.contrib import admin

from .models import Article, Question, Choice

admin.site.register(Article)
admin.site.register(Question)
admin.site.register(Choice)

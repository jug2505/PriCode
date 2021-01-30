from django.shortcuts import render
from django.http import HttpResponse

from .models import Course


def home_page(request):
    return render(request, 'courses/home.html')

def courses(request, course_id):
    pass

# Вот так возвращать template c контекстом
# return render(request, 'home.html', context)
# context - словарь
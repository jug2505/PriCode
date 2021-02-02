from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from courses.views import home_page

from .models import Article, Question, Choice


class HomePageTest(TestCase):
    
    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'courses/home.html')
    
class AddPageTest(TestCase):

    def test_article_adding(self):
        response = self.client.post('article_add', data={
            'article_title': 'title',
            'article_text': 'text',

            'question1_text': 'Who?',
            'q1_choice1_text' : 'Nobody',
            'q1_choice2_text' : 'No',
            'q1_choice3_text' : 'Yes',
            'q_1choice4_text' : 'Not sure',
            'blankRadio1' : '1',

            'question2_text': 'Who?',
            'q2_choice1_text' : 'Nobody',
            'q2_choice2_text' : 'No',
            'q2_choice3_text' : 'Yes',
            'q2_choice4_text' : 'Not sure',
            'blankRadio2' : '1',

            'question3_text': 'Who?',
            'q3_choice1_text' : 'Nobody',
            'q3_choice2_text' : 'No',
            'q3_choice3_text' : 'Yes',
            'q3_choice4_text' : 'Not sure',
            'blankRadio3' : '1'})

        print(len(Article.objects.all()))

        self.assertEqual(response.status_code, 302)
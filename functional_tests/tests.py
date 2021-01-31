from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time

class NewVisitorTest(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()
    
    def test_user_can_pass_courses(self):
        
        # Виталий услышал о новом крутом супераппе в образовании
        # Он заходит на главную страницу, чтобы заценить его
        
        # Он видит перед собой список статей
        
        # Он нажимает на первую статью
        
        # Страница переходит на другой адрес
        # На новой странице показана статья, на которую нажал Виталий
        # Название статей совпадают
        
        # На странице есть тест по содержимому статьи
        # Виталий наугад нажимает на радиокнопки
        
        # После страница переходить на другой адрес 
        # Виталий видит результат своего теста
        
        # Радостный, он идёт спать
        self.fail('Доделать тест')  

    def test_user_can_add_course(self):
        
        # Татьяна хочет добавить свою статью
        # Она нажимает на кнопку добавления статьи
        
        # Открывается форма, Татьяна заполняет поля
        
        # После отправки формы в
        # списке статей добавилась Татьянина
        self.fail('Доделать тест')
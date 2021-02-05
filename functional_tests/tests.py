from django.test import LiveServerTestCase
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_user_can_pass_courses(self):
        # Если при запуске браузера сразу будет хотя бы одна статья, перенсти код из другого теста
        self.fail('Доделать тест')

    def test_user_can_add_course(self):

        # Татьяна заходит на сайт
        self.browser.get(self.live_server_url)

        # Татьяна хочет добавить свою статью
        # Она нажимает на кнопку добавления статьи
        self.browser.find_element_by_link_text('Добавить статью').click()
        time.sleep(4)

        # Открывается форма, Татьяна заполняет поля
        self.browser.find_element_by_name('article_title').send_keys('Title')
        self.browser.find_element_by_name('article_text').send_keys('Text')

        self.browser.find_element_by_name('question1_text').send_keys('Who?')
        self.browser.find_element_by_name('q1_choice1_text').send_keys('Nobody')
        self.browser.find_element_by_name('q1_choice2_text').send_keys('No')
        self.browser.find_element_by_name('q1_choice3_text').send_keys('Yes')
        self.browser.find_element_by_name('q1_choice4_text').send_keys('Not sure')
        self.browser.find_element_by_id('blankRadio1_1').click()

        time.sleep(4)

        self.browser.find_element_by_name('question2_text').send_keys('Why?')
        self.browser.find_element_by_name('q2_choice1_text').send_keys('Because')
        self.browser.find_element_by_name('q2_choice2_text').send_keys('No')
        self.browser.find_element_by_name('q2_choice3_text').send_keys('Yes')
        self.browser.find_element_by_name('q2_choice4_text').send_keys('Not sure')
        self.browser.find_element_by_id('blankRadio2_2').click()

        time.sleep(1)

        self.browser.find_element_by_name('question3_text').send_keys('How much?')
        self.browser.find_element_by_name('q3_choice1_text').send_keys('Many')
        self.browser.find_element_by_name('q3_choice2_text').send_keys('1')
        self.browser.find_element_by_name('q3_choice3_text').send_keys('2')
        self.browser.find_element_by_name('q3_choice4_text').send_keys('More than 3')
        self.browser.find_element_by_id('blankRadio3_3').click()

        time.sleep(4)

        self.browser.find_element_by_name('q3_choice4_text').send_keys(Keys.ENTER)

        time.sleep(4)

        # После отправки формы в
        # списке статей добавилась Татьянина

        title = self.browser.find_element_by_class_name('card-title').text
        self.assertEqual(title, 'Title')

        text = self.browser.find_element_by_class_name('card-text').text
        self.assertEqual(text, 'Text')

        ##########################################################################
        # Так как при запуске теста на проверку работы статьи и теста, нужна хотя бы одна статья, то
        # Объединил тесты в один, если будет хотя бы одна статья, то весь нижний текст, можно перенести в верхний тест
        # Виталий услышал о новом крутом супераппе в образовании
        # Он заходит на главную страницу, чтобы заценить его
        # Он видит перед собой список статей
        # Он нажимает на первую статью

        self.browser.find_element_by_link_text('Ссылка на статью').click()

        time.sleep(4)

        # Страница переходит на другой адрес
        # На новой странице показана статья, на которую нажал Виталий
        # Название статей совпадают

        title2 = self.browser.find_element_by_xpath('/html/body/div/h1[1]').text
        text2 = self.browser.find_element_by_xpath('/html/body/div/p').text
        self.assertEqual(title, title2)
        self.assertEqual(text, text2)

        # На странице есть тест по содержимому статьи
        # Виталий наугад нажимает на радиокнопки

        self.browser.find_element_by_xpath('/html/body/div/form/div/input[1]').click()
        self.browser.find_element_by_xpath('/html/body/div/form/div/input[5]').click()
        self.browser.find_element_by_xpath('/html/body/div/form/div/input[9]').click()

        # После страница переходить на другой адрес

        self.browser.find_element_by_xpath('/html/body/div/form/input[2]').click()

        # Виталий видит результат своего теста
        # Радостный, он идёт спать

        time.sleep(4)
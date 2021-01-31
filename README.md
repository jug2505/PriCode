# PriCode
Суперапп в образовании

- User Stories - В файле functional_tests/tests.py

Для фронта:

- home.html:
    
    article_titles: Массив названий статей

    article_texts: Массив обрезанных статей

    article_ids: Массив id статей

Схема БД:

- Article:
    
    article_title: String 
    
    article_text : String

- Question:
    
    article: ForeignKey(Article)
    
    question_text: String

- Choice:
   
    question: ForeignKey(Question)
   
    choice_text: String
   
    choise_isRight: Boolean
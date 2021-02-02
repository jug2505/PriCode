# PriCode
Суперапп в образовании

- User Stories - В файле functional_tests/tests.py

Для фронта:

- home.html:

    articles: Массив статей для показа на главной
    
    articles.article_titles: Название

    articles.article_texts: Текст

    articles.article_ids: id статьи

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
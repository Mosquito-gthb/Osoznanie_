"""
URL configuration for backend_conference_rguk_08_04_26 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views # Импортируем views.py из этой же папки

urlpatterns = [
    # ... другие пути, если есть ...

    # Путь для отправки ответов на тест (например, list_1)
    # <str:test_slug> - это переменная часть адреса, которая примет значение 'list_1'
    path('<str:test_slug>/submit/', views.submit_answers_view, name='submit_answers'), 

    # Путь для отображения страницы результата
    path('test/result/<int:result_id>/', views.result_view, name='result'), 
]
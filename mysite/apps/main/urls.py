from django.urls import path

from . import views

app_name = 'quest'

urlpatterns = [
    path('', views.index, name = 'index'),

    path('task_1/', views.task1, name = 'task1'),
    path('task_2/', views.task2, name = 'task2'),
    path('task_3/', views.task3, name = 'task3'),
    path('task_4/', views.task4, name = 'task4'),
    path('task_5/', views.task5, name = 'task5'),

    path('info_1/answer', views.answer1, name = 'answer1'),
    path('info_2/answer', views.answer2, name = 'answer2'),
    path('info_3/answer', views.answer3, name = 'answer3'),
    path('info_4/answer', views.answer4, name = 'answer4'),
    path('info_5/answer', views.answer5, name = 'answer5'),
    path('task_5/value', views.value, name = 'value'),


    path('info_1/', views.info1, name = 'info1'),
    path('info_2/', views.info2, name = 'info2'),
    path('info_3/', views.info3, name = 'info3'),
    path('info_4/', views.info4, name = 'info4'),
    path('info_5/', views.info5, name = 'info5'),

    path('final/', views.final, name = 'final'),
]

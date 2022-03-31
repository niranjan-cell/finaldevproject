from django.urls import path

from Quiz import views

urlpatterns=[
    path('take-test',views.Take_Test,name="take_test"),
    path('show-ques',views.ShowQues,name="show_question"),
    path('quiz-details',views.Show_details,name="quiz-details"),
]
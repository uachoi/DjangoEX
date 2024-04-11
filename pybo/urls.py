from django.urls import path
from . import views # 현재 패키지에서 views 모듈을 가져옴

app_name='pybo'

urlpatterns=[
    # config/urls.py에서 pybo/에 대한 처리를 먼저 하고 실행되므로, 첫 번째 매개변수에 빈 문자열을 인자로 넘겨줌
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),    ## 추가
]
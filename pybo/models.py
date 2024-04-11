from django.db import models

# 질문 모델 클래스
class Question(models.Model):
    subject = models.CharField(max_length=200)  # 질문 제목
    content = models.TextField()    # 질문 내용
    create_date = models.DateTimeField()    # 질문 작성 일시 (날짜, 시간)
    
    def __str__(self):
        return self.subject


# 답변 모델 클래스
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)    # 질문
    content = models.TextField()    # 답변 내용
    create_date = models.DateTimeField()    # 답변 작성 일시
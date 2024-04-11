from django import forms
from pybo.models import Question

class QuestionForm(forms.ModelForm):        ## ModelForm을 상속받은 클래스 작성
    class Meta:	        ## 내부 클래스로 Meta 클래스 정의
        model = Question        ## 모델 폼에서 사용할 모델, 모델의 필드 지정
        fields = ['subject', 'content']

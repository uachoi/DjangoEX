from django.shortcuts import render, get_object_or_404, redirect

#from django.http import HttpResponse
from .models import Question    ## 데이터 작성일시 역순 조회
from django.utils import timezone

from .forms import QuestionForm ##추가

def index(request):
    
    question_list=Question.objects.order_by('-create_date') ## 데이터 작성일시 역순 조회
    context={'question_list': question_list}
    ##return HttpResponse("안녕하세요 pybo에 오신 것을 환영합니다.")
    
    return render(request, 'pybo/question_list.html', context)    ## render로 화면 출력

def detail(request, question_id):
    ## question=Question.objects.get(id=question_id)
    question=get_object_or_404(Question,pk=question_id)
    context={'question': question}
    
    return render(request, 'pybo/question_detail.html', context)

def answer_create(request, question_id):            ## question_id : URL 매핑 정보값이 넘어옴 / request : 입력한 데이터
    question=get_object_or_404(Question, pk=question_id)        ## 답변 추가할 질문 조회
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    
    return redirect('pybo:detail', question_id=question.id)     ## 답변 추가 후 상세 페이지로 리다이렉트


# def question_create(request):       ## QuestionForm(장고 폼) 클래스로 생성한 객체 form을 사용한다
#     form=QuestionForm()
#     return render(request, 'pybo/question_form.html', {'form':form})    ## render 함수에 전달한 {'form':form} : 템플릿에서 엘리먼트 생성 시 사용

def question_create(request):
    if request.method == 'GET':     # 요청 방식이 GET : 입력 화면 반환
        form = QuestionForm()
        return render(request, 'pybo/question_form.html', { 'form': form })
    elif request.method == 'POST':
        # POST 방식 : 요청 본문을 통해 전달된 입력값 저장  / 내용 저장 후 리다이렉트
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('pybo:index')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionForm, AnswerForm

from django.core.paginator import Paginator

# Create your views here.


def question_list(request):
    """전체 질문 추출"""

    # 현재 페이지 번호 가져오기
    # request.요청이오는방식.get("변수이름", 없으면 넣어줄 기본값)
    page = request.GET.get("page", 1)

    # questions = Question.objects.all()
    questions = Question.objects.order_by("-created_at")

    pagenator = Paginator(questions, 10)
    page_obj = pagenator.get_page(page)

    return render(request, "board/question_list.html", {"questions": page_obj})


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)
    context = {"question": question}
    return render(request, "board/question_detail.html", context)


def answer_create(request, qid):
    """답변등록"""
    question = get_object_or_404(Question, id=qid)

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.save()
            return redirect("board:question_detail", qid=qid)
    # 실패 시 get 방식으로 처리
    else:
        form = AnswerForm()
    # Answer.objects.create(question=question, content=request.POST.get("content"))

    # question.answer_set.create(content=request.POST.get("content"))

    # answer = Answer(question=question, content=request.POST.get("content"))
    # answer.save()

    # 실패 시 get 방식으로 처리
    context = {"question": question, "form": form}
    return render(request, "board/question_detail.html", context)


def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})

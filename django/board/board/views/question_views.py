from django.shortcuts import render, get_object_or_404, redirect
from ..models import Question
from ..forms import QuestionForm

from django.contrib.auth.decorators import login_required

from django.utils import timezone

# Create your views here.


@login_required(login_url="common:login")
def question_create(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            # 중간저장 느낌
            question = form.save(commit=False)
            # 작성자 = 로그인 유저
            question.author = request.user
            question.save()
            return redirect("board:question_list")
    else:
        form = QuestionForm()
    return render(request, "board/question_form.html", {"form": form})


@login_required(login_url="common:login")
def question_modify(request, qid):
    question = get_object_or_404(Question, id=qid)
    # qid 에 해당하는 questtion 찾은 후
    # 변경할 부분 수정후 save()
    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.modifed_at = timezone.now()
            question.save()
            return redirect("board:question_detail", qid=qid)

    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_form.html", {"form": form})


@login_required(login_url="common:login")
def question_delete(request, qid):
    question = get_object_or_404(Question, id=qid)
    question.delete()
    return redirect("board:question_list")

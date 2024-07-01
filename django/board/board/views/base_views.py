from django.shortcuts import render, get_object_or_404

# from board.models import Question
from ..models import Question, QuestionCount
from tools.utils import get_client_ip


from django.core.paginator import Paginator

from django.db.models import Q, Count  # Q : or 조건으로 데이터 조회 시키려고 씀

# Create your views here.


def question_list(request):
    """전체 질문 추출"""

    # 현재 페이지 번호 가져오기
    # request.요청이오는방식.get("변수이름", 없으면 넣어줄 기본값)
    page = request.GET.get("page", 1)
    # 검색어
    keyword = request.GET.get("keyword", "")
    # 정렬기준
    so = request.GET.get("so", "recent")

    # questions = Question.objects.all() # 전체 리스트를 뽑고
    # questions = Question.objects.order_by("-created_at")
    if so == "recommend":  # 추천수
        # num_voter 라는 컬럼명으로 voter를 Count 한걸 임시로 저장해줘
        questions = Question.objects.annotate(num_voter=Count("voter")).order_by(
            "-num_voter", "-created_at"
        )
    elif so == "popular":  # 답변수
        questions = Question.objects.annotate(num_answer=Count("answer")).order_by(
            "-num_answer", "-created_at"
        )
    else:
        questions = Question.objects.order_by("-created_at")

    # 뽑은 리스트에서 필터를 검
    if keyword:
        questions = questions.filter(
            Q(subject__icontains=keyword)
            | Q(content__icontains=keyword)
            | Q(author__username__icontains=keyword)
            | Q(answer__author__username__icontains=keyword)
        ).distinct()

    pagenator = Paginator(questions, 10)
    page_obj = pagenator.get_page(page)
    context = {"questions": page_obj, "page": page, "keyword": keyword, "so": so}
    return render(request, "board/question_list.html", context)


def question_detail(request, qid):
    question = get_object_or_404(Question, id=qid)

    # 클라이언트 ip 가져오기
    ip = get_client_ip(request)
    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()

    if cnt == 0:
        # QuestionCount 객체 생성 후 저장
        qc = QuestionCount(ip=ip, question=question)
        qc.save()
        # Question view_cnt + 1
        if question.view_cnt:
            question.view_cnt += 1
        else:
            question.view_cnt = 1
        question.save()

    # 현재 페이지 번호 가져오기
    page = request.GET.get("page", 1)
    # 검색어
    keyword = request.GET.get("keyword", "")
    # 정렬기준
    so = request.GET.get("so", "recent")

    context = {"question": question, "page": page, "keyword": keyword, "so": so}
    # "user": request.user
    return render(request, "board/question_detail.html", context)

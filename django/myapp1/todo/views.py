from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo


# Create your views here.
# 서비스 작업도 같이함
def list(request):
    """
    html 응답
    """
    # 전체 칼럼 다 가지고오기
    # todos = Todo.objects.all()
    todos = Todo.objects.filter(completed=False)
    return render(request, "todo/todo_list.html", {"todos": todos})


def create(request):
    """
    get/post 둘다 처리
    """
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        important = request.POST.get("important")
        print("전송내용", title, description, important)

        if important:
            todo = Todo(title=title, description=description, important=important)
        else:
            todo = Todo(title=title, description=description)
        todo.save()
        return redirect("list")
    return render(request, "todo/todo_create.html")


def read(request, id):
    # todo = Todo.objects.get(id=id)
    todo = get_object_or_404(Todo, id=id)
    return render(request, "todo/todo_detail.html", {"todo": todo})


def done(request, id):
    # 수정할 model 찾기
    todo = Todo.objects.get(id=id)
    # 변경 내용 삽입
    todo.completed = True
    todo.save()

    return redirect("list")


def done_list(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, "todo/todo_done_list.html", {"dones": dones})


def edit(request, id):
    todo = Todo.objects.get(id=id)

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        important = request.POST.get("important")

        todo.title = title
        todo.description = description
        if important:
            todo.important = important
        else:
            todo.important = False

        todo.save()
        return redirect("read", id=id)

    return render(request, "todo/todo_edit.html", {"todo": todo})


# def list(request):
#     """
#     일반문자열 응답
#     """
#     return HttpResponse("Hello")

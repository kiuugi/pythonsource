from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def list(request):
    """
    html 응답
    """
    return render(request, "todo/todo_list.html")


# def list(request):
#     """
#     일반문자열 응답
#     """
#     return HttpResponse("Hello")

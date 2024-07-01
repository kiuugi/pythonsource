from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .froms import PostForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator


# Create your views here.
@login_required(login_url="common:login")
def list(request):
    # Post 전체 조회
    page = request.GET.get("page", 1)

    posts = Post.objects.all()

    paginator = Paginator(posts, 5)
    page_obj = paginator.get_page(page)

    context = {"posts": page_obj}

    return render(request, "blog/list.html", context)


def detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    return render(request, "blog/post.html", {"post": post})


def create(request):
    if request.method == "POST":
        # 폼에 post 로 넘어오는 내용 담기
        form = PostForm(request.POST, request.FILES)
        # 폼 유효성 검증
        if form.is_valid():
            # 유효성 통과시 저장
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            # 리스트로 이동
            return redirect("blog:list")
        # return redirect("blog:detail", post.id)
    else:
        form = PostForm()

    return render(request, "blog/create.html", {"form": form})


def modify(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect("blog:detail", post.id)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/modify.html", {"form": form, "post": post})


def delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    post.delete()

    return redirect("blog:list")

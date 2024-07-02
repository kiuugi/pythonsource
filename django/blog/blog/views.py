from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .froms import PostForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
@login_required(login_url="common:login")
def list(request):
    # Post 전체 조회
    page = request.GET.get("page", 1)

    posts = Post.objects.all()

    paginator = Paginator(posts, 5)  # posts를 5개씩 가져감
    page_obj = paginator.get_page(page)

    context = {"posts": page_obj}

    return render(request, "blog/list.html", context)


def detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    # 로그인 유저가 해당 게시물에 좋아요 했는지 여부
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(request, "blog/post.html", {"post": post, "is_liked": is_liked})


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

            # 태그 저장 (다른 테이블에 있어서 저장해줘야함)
            form.save_m2m()

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


def comment_create(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        content = request.POST.get("content")

        # Comment.objects.create(user=request.user, post=post, content=content)
        comment = Comment(user=request.user, post=post, content=content)
        comment.save()
        return redirect("blog:detail", post_id)

    else:

        return redirect("blog:detail", post_id)


def post_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    is_liked = post.likes.filter(id=request.user.id).exists()

    is_liked_change = False

    if is_liked:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)  # 기본 중복X
        is_liked_change = True

    return JsonResponse({"likes": post.likes.count(), "is_liked": is_liked_change})

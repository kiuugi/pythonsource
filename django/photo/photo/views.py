from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from .forms import PhotoForm


# Create your views here.
def list(request):
    photos = Photo.objects.all()

    return render(request, "photo/photo_list.html", {"photos": photos})


def create(request):
    if request.method == "POST":
        form = PhotoForm(request.POST)
        # print("post", form) 이건 서버 연결한 터미널에서 나옴
        if form.is_valid():  # 유효성검증(모델에 정의된 규칙)
            form.save()  # model.save() 호출됨
            return redirect("photo_list")
    else:
        form = PhotoForm()

    return render(request, "photo/photo_create.html", {"form": form})


def detail(request, id):
    photo = get_object_or_404(Photo, id=id)
    return render(request, "photo/photo_detail.html", {"photo": photo})


def remove(request, id):
    photo = get_object_or_404(Photo, id=id)
    photo.delete()

    return redirect("photo_list")


def edit(request, id):
    photo = get_object_or_404(Photo, id=id)
    if request.method == "POST":
        form = PhotoForm(
            request.POST, instance=photo
        )  # request.POST 수정된내용 instance=photo 원본내용
        if form.is_valid():
            form.save()
            return redirect("photo_detail", id=id)
    else:
        form = PhotoForm(instance=photo)

    return render(request, "photo/photo_edit.html", {"form": form})

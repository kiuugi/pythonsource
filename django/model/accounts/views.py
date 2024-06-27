from django.shortcuts import render
from .forms import UsersForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = UsersForm()

    return render(request, "register.html", {"form": form})


def index(request):
    return render(request, "index.html")

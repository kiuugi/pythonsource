from django.shortcuts import render, redirect
from .forms import UsersForm


# Create your views here.
def register(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("common:login")

    else:
        form = UsersForm()

    return render(request, "common/register.html", {"form": form})




from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .form import ImageForm
from .models import Image


# Create your views here.

@login_required
def index(request):
    if request.method == "POST":

        form = ImageForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.user = request.user
            form.save()
            obj = form.instance
        return render(request, "Project.html", {"obj": obj})
    else:
        if request.user.is_authenticated:
            form = ImageForm(instance=request.user)
        img = Image.objects.all()
        return render(request, "Project.html", {"img": img, "form": form})

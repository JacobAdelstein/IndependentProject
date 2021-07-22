from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from django.shortcuts import render, HttpResponse
from .form import ImageForm
from .models import Image



# Create your views here.

@login_required
def index(response):
    if response.method == "POST":

        form = ImageForm(data=response.POST, files=response.FILES)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Image(name=n)
            t.save()
            form.save()
            obj = form.instance
            response.user.image.add(t)
        return render(response, "Project.html", {"obj": obj})
    else:
        form = ImageForm()
        img = Image.objects.all()
        return render(response, "Project.html", {"img": img, "form": form})

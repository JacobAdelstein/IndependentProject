from django.shortcuts import render
from .models import Description

# Create your views here.







def home(request):
    return render(request, 'home.html')

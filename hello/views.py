from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def hello(request):
    users = User.objects.all()
    return render(request, "home.html", {'users': users})

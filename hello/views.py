from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Member
from .forms import MemberForm

def hello(request):
    users = User.objects.all()
    members = [member.username for member in Member.objects.all()]
    return render(request, "home.html", {'users': users, 'members': members})


def member_create_view(request):
    form = MemberForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('hello')

    context = {
        'form': form
    }
    return render(request, "create_member.html", context)

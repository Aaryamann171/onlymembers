from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Member
from .forms import MemberForm


def home_view(request):
    users = User.objects.all()
    members = [member.username for member in Member.objects.all()]
    return render(request, 'home.html', {'users': users, 'members': members})


def member_create_view(request):
    form = MemberForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(request, f'new member created: {username}')
        return redirect('home')
    else:
        messages.error(request, "something went wrong, try again")

    context = {
        'form': form
    }
    return render(request, 'create_member.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'new user added: {username}')
            login(request, user)
            messages.info(request, f'logged in as {username}')
            return redirect('home')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

            context = {'form': form}
            return render(request, "register.html", context)

    form = UserCreationForm
    context = {'form': form}
    return render(request, 'register.html', context)


def logout_request(request):
    logout(request)
    messages.info(request, 'logged out successfully')
    return redirect('home')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usr = form.cleaned_data.get('username')
            passw = form.cleaned_data.get('password')
            user = authenticate(username=usr, password=passw)
            if user is not None:
                login(request, user)
                messages.info(request, f'logged in as {usr}')
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")

        else:
            messages.error(request, "Invalid username or password.")

    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'login.html', context)

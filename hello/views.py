from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Member
from .forms import MemberForm
from django.views.generic import CreateView, UpdateView, DetailView


def home_view(request):
    users = User.objects.all()
    members = [member.username for member in Member.objects.all()]
    return render(request, 'home.html', {'users': users, 'members': members})


class MemberCreateView(CreateView):
    template_name = 'member_create.html'
    form_class = MemberForm
    queryset = Member.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class MemberUpdateView(UpdateView):
    template_name = 'member_create.html'
    form_class = MemberForm
    queryset = Member.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class MemberDetailView(DetailView):
    template_name = 'member_details.html'
    queryset = Member.objects.all()

def member_delete_view(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'delete_member.html', context)

def confirm_delete(request, id):
    obj = Member.objects.filter(id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('home')
    else:
        context = {'obj':obj}
        return render(request, 'confirm_delete.html', context)

def member_update_view(request):
    members = Member.objects.all()
    context = {'members': members}
    return render(request, 'update_member.html', context)

class MemberUpdate(UpdateView):
    model = Member
    fields = ['name']
    queryset = Member.objects.all()

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

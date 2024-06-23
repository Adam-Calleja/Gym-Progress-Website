from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GymUserCreationForm, LoginForm
from django.views import View

class Index(View):
    def get(self, request):
        return render(request, 'core/index.html')

class Account(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user

        context = {
            user:user
        }

        return render(request, 'core/account.html', context)

class Register(View):
    def post(self, request):
        form = GymUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            
            return redirect('/')
        return render(request, 'core/register.html', {'form': form})
    
    def get(self, request):
        form = GymUserCreationForm()

        return render(request, 'core/register.html', {'form': form})

class LogIn(View):
    def post(self, request):
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            
            return redirect('core/index.html')
        
        return render(request, 'core/login.html', {'form': form})
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core/account.html')
        else: 
            form = LoginForm()
            return render(request, 'core/login.html', {'form': form})

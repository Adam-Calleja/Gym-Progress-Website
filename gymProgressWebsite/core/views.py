from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import GymUserCreationForm, LoginForm
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

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
            
            return HttpResponseRedirect(reverse("core:index"))

        return HttpResponseRedirect(reverse("core:register", args=({'form': form,})))
    
    def get(self, request):
        form = GymUserCreationForm()

        return render(request, 'core/register.html', {'form': form})

class LogIn(View):
    def post(self, request):
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            
            return HttpResponseRedirect(reverse("core:index"))
        
        return HttpResponseRedirect(reverse("core:login", args=({"form": form, })))
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('core:account')
        else: 
            form = LoginForm()
            return render(request, 'core/login.html', {'form': form})

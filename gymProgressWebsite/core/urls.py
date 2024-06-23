from django.urls import path
from core.views import Index, Account, LogIn, Register


urlpatterns = [
    path("", Index.as_view()),
    path("login/", LogIn.as_view()),
    path("account/", Account.as_view()),
    path("register/", Register.as_view()),
]
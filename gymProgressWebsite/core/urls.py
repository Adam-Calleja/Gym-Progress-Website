from django.urls import path
from core.views import Index, Account, LogIn, Register


urlpatterns = [
    path("", Index.as_view(), name="index"),
    path("login/", LogIn.as_view(), name="login"),
    path("account/", Account.as_view(), name="account"),
    path("register/", Register.as_view(), name="register"),
]
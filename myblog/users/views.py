from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login
from .forms import CustomerUserCreationForm


def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request: HttpRequest):
    if request.method == "GET":
        return render(
            request,
            "users/register.html",
            {"form": CustomerUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("users:dashboard"))


class MyLoginView(LoginView):
    template_name = "users/registration/login.html"


class MyPasswordChangeView(PasswordChangeView):
    template_name = "users/registration/my_password_change_form.html"
    success_url = reverse_lazy("users:password_change_done")


class MyPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = "users/registration/my_password_change_done.html"

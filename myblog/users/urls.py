from django.urls import path, include
from users import views

app_name="users"
urlpatterns = [
    path("dashboard/", views.dashboard, name="dashboard"),
    path("accounts/login/", views.MyLoginView.as_view(), name="login"),
    path("accounts/password_change/", views.MyPasswordChangeView.as_view(), name="password_change"),
    path("accounts/password_change/done/", views.MyPasswordChangeDoneView.as_view(), name="password_change_done"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.register, name="register"),
]
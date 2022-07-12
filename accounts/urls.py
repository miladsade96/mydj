from django.urls import path
from accounts.views import login_view, signup_view

# Defining app name
app_name = "accounts"

urlpatterns = [
    path("login", login_view, name="login"),
    # path("logout", logout_view, name="logout"),
    path("signup", signup_view, name="signup"),
]

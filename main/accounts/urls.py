from django.urls import path, include
from accounts import views

urlpatterns = [
    path("sign-up/", views.signup_view, name="sign_up_url"),
    path("login/", views.login_view, name="login_url"),
    path("logout/", views.logout_view, name="logout_url"),
    path("edit-user/<str:username>/", views.user_actions, name="edit_user_url")
]
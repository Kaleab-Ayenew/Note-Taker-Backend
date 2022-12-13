from django.urls import path, include
from accounts import views

urlpatterns = [
    path("sign-up/", views.signup_view),
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("edit-user/<str:username>/", views.user_actions)
]
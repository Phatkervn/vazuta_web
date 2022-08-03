from django.urls import path , include
from .views import register_request ,login_request,logout_request,profile_user
urlpatterns = [
    path("register",register_request),
    path("login", login_request),
    path("logout",logout_request),
    path("",profile_user)
]

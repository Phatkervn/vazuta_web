from django.urls import path , include
from .views import home_index , view_app , search , app ,about
urlpatterns = [
    path("",home_index,name="homepage"),
    path("view/<int:ID>", view_app),
    path("search" , search),
    path("app/<str:type>" , app),
    path("about",about)
]
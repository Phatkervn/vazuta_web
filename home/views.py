from django.shortcuts import render , get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required 
from django.http import HttpResponse
from django.db.models import Q
from .models import App

def home_index(request):

    app_hot = App.objects.filter(appType__contains="hot")[:3]
    game_mod = App.objects.filter(appType__contains="game_mod")
    game_pc = App.objects.filter(appType__contains="game_pc")
    game_mobile = App.objects.filter(appType__contains="game_mobile")
    app_mobile = App.objects.filter(appType__contains="app_mobile")
    tool = App.objects.filter(appType__contains="tool")
    return render(
        request=request, 
        template_name="home/index.html",
        context={
            "app_hot" : app_hot , 
            "game_pc":game_pc ,
            "game_mod":game_mod ,
            "game_mobile":game_mobile,
            "app_mobile" : app_mobile ,
            "tool":tool,
        }
    )


def view_app(request,ID):
    app = App.objects.filter(pk=ID)
    return render(
        request=request, 
        template_name="home/appview.html",
        context={
            "app" : app
        }
    )

def search(request):
    if request.method == "POST":
        query = request.POST.dict().get("searchQuery")
        #resultObj = App.objects.filter(Q(appName__search=str(query)))
        return render(
            request,
            template_name="home/search.html",
            context={

            }
        )


def app(request,type):
    app_new = App.objects.filter(appType__contains=str(type))
    return render(
        request,
        template_name="home/app.html" , 
        context={
            "apps": app_new , 
            "type" : type
        }
    )

def about(request):
    return render(
        request,
        template_name="home/about.html"
    )

def auto_Up(request):
    if request.method == "POST":
        pass
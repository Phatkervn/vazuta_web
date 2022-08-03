from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login ,authenticate , logout 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.forms import AuthenticationForm
def register_request(request):
	if request.user.is_authenticated:
		return redirect("/user")
	else:
		if request.method == "POST":
			form = NewUserForm(request.POST)
			if form.is_valid():
				user = form.save()
				login(request, user)
				
				return redirect("homepage")
			
		form = NewUserForm()
		return render (request=request, template_name="account/register.html", context={"register_form":form})


def login_request(request):
	if request.user.is_authenticated:
		return redirect("/user")
	else:
		if request.method == "POST":
			form = AuthenticationForm(request, data=request.POST)
			if form.is_valid():
				username = form.cleaned_data.get('username')
				password = form.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					
					return redirect("homepage")
				else:
					# messages.error(request,"Invalid username or password.")
					pass
			else:
				# messages.error(request,"Invalid username or password.")
				pass
		form = AuthenticationForm()
		return render(request=request, template_name="account/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	
	return redirect("homepage")



@login_required
def profile_user(request):
	return render(request=request, template_name="account/profile.html")
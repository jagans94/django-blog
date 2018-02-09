from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.
def signup_view(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			# log the user in
			return redirect('accounts:signin')
	else:
		form = UserCreationForm()

	context = {
		'form' : form
		}
	return render(request,'accounts/signup.html',context)

def signin_view(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# log the user in
			user = form.get_user()
			login(request,user)
			if 'next' in request.POST:
				return redirect(request.POST.get('next'))
			return redirect('articles:list')
	else:
		form = AuthenticationForm()

	context = {
		'form' : form
		}
	return render(request,'accounts/signin.html',context)

def signout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('articles:list')

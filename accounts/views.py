from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.
def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			# log the user in
			return redirect('home')
	else:
		form = UserCreationForm()

	context = {
		'form' : form
		}
	return render(request,'accounts/signup.html',context)

def signin(request):
	if request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			# log the user in
			return redirect('home')
	else:
		form = AuthenticationForm()

	context = {
		'form' : form
		}
	return render(request,'accounts/signin.html',context)

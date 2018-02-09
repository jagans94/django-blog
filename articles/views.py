from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms
		
# Create your views here.

def articles(request):
	articles = Article.objects.all().order_by('date')
	context = {
		"articles" : articles
	}
	return render(request,'articles/articles.html',context)

def article_details(request,slug):
	#return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	context = {
		"article" : article
	}
	return render(request,'articles/article_details.html',context)

@login_required(login_url='accounts:signin')
def article_create(request):
	if request.method == 'POST':
		form = forms.CreateArticle(request.POST,request.FILES)
		if form.is_valid():
			# save to db	
			return redirect('articles:list')
	else:
		form = forms.CreateArticle()
	context = {
	'form' : form
	}
	return render(request,'articles/article_create.html',context)


from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.

def articles(request):
	articles = Article.objects.all().order_by('date')
	context = {
		"articles" : articles
	}
	return render(request,'articles/articles.html',context)

def article_details(request,slug):
	return HttpResponse(slug)
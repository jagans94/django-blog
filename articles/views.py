from django.shortcuts import render
from .models import Article

# Create your views here.

def articles(request):
	articles = Article.objects.all().order_by('date')
	context = {
		"articles" : articles
	}
	return render(request,'articles/articles.html',context)
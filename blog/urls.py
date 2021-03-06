from django.contrib import admin
from django.urls import path, re_path, include

from .import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf.urls.static import static
from django.conf import settings

import articles

urlpatterns = [ 
	path('',views.home, name='home'),
    path('admin/', admin.site.urls),	
    path('about/',views.about),
    path('articles/',include('articles.urls')),
    path('accounts/',include('accounts.urls')),
    ]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


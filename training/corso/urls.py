from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home-corso'),
    path('article-details/', views.article, name='article'),
    path('privacy-policy/', views.privacy, name='privacy-policy'),
    path('terms-conditions/', views.conditions, name='terms-conditions'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
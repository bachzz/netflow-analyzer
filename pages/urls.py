# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView, upload

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('upload/', upload, name='upload')
]
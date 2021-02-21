from django.urls import path
from .views import dashboard_view, add_flow


urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('add/', add_flow)
]
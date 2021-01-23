from django.urls import path
from .views import weather

app_name = 'weather'

urlpatterns = [
    path('',weather),
]
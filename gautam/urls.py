
from django.contrib import admin
from django.urls import path, include

from todo.views import todo_list
from weather.views import weather

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('weather.urls', namespace='weather')),
]

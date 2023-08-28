from django.contrib import admin
from django.urls import path
from helloWorld.views import hello_world
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world)
]

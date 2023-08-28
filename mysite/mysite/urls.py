from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('CCB_app/', include('CCB_app.urls')),
    path('admin/', admin.site.urls),
]
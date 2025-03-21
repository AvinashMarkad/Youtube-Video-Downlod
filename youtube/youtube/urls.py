
from django.contrib import admin
from django.urls import path
from downloader import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.download_video, name='download_video'),   
]
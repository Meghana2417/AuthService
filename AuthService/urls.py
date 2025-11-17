#from django.urls import path, include

#urlpatterns = [
 #   path('api/auth/', include('authapp.urls')),
#]
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Auth Service is running!")

urlpatterns = [
    path("", home),                      #  Fix for "/"
    path("api/auth/", include("authapp.urls")),   # your auth app
]

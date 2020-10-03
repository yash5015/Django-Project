from django.contrib import admin
from django.urls import path
from.views import Index,bbc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name="Index"),
    path('bbc/',bbc,name="bbc"),
]

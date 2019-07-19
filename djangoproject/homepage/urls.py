from django.contrib import admin
from django.urls import path, include
import myapp.views
import myaccount.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="home"),
    path('index/', myapp.views.index, name="index"),
    path('accounts/',include('myaccount.urls')),
]
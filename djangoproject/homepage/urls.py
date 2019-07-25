from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="home"),
    path('index/', myapp.views.index, name="index"),
    path('support/',myapp.views.support, name="support"),
    path('support/pop_tnr',myapp.views.pop_tnr, name="pop_tnr"),
    path('support/pop_snack',myapp.views.pop_snack, name="pop_snack"),

]

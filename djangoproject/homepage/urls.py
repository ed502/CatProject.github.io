from django.contrib import admin
from django.urls import path
import myapp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="home"),
    path('index/', myapp.views.index, name="index"),
    path('board_free/', myapp.views.board_free, name="board_free"),
    path('board_detect/', myapp.views.board_detect, name="board_detect"),
]

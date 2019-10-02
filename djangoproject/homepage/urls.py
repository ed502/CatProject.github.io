from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
import myapp.views
import myaccount.views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="home"),
    path('index/', myapp.views.index, name="index"),
    path('board_free/', myapp.views.board_free, name="board_free"),
    path('board_detect/', myapp.views.board_detect, name="board_detect"),
    path('create_free/', myapp.views.create_free, name="create_free"),
    path('create_detail/', myapp.views.create_detail, name="create_detail"),
    path('newPost', myapp.views.create, name="newPost"),
    path('', myapp.views.read, name="freelist"),
    path('detail/<int:free_list_id>', myapp.views.detail, name="detail"),
    path('accounts/',include('myaccount.urls')),
    path('support/',myapp.views.support, name="support"),
    path('support/pop_tnr',myapp.views.pop_tnr, name="pop_tnr"),
    path('support/pop_snack',myapp.views.pop_snack, name="pop_snack"),
    path('support/support_success',myapp.views.support_success, name="support_success"),
    path('support/support_success2',myapp.views.support_success2, name="support_success2"),
    path('create/', myapp.views.create, name="create"),
    path('location/<str:loc_str>/newMap/', myapp.views.newMap, name="newMap"),
    path('location/', myapp.views.location, name="location"),
    path('location/<str:loc_str>/', myapp.views.loc_cat, name="loc_cat"),
    path('pay/', myapp.views.pay, name="pay"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

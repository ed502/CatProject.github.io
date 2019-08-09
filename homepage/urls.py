from django.contrib import admin
from django.urls import path, include
import myapp.views
import myaccount.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="home"),
    path('index/', myapp.views.index, name="index"),
    path('map/', myapp.views.map, name="map"),
    path('create/', myapp.views.create, name="create"),
    path('location/<str:loc_str>/newMap/', myapp.views.newMap, name="newMap"),
    path('location/', myapp.views.location, name="location"),
    path('location/<str:loc_str>/', myapp.views.loc_cat, name="loc_cat"),
    path('detailMap/<int:cat_id>/', myapp.views.detailMap, name="detailMap"),
    path('accounts/',include('myaccount.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
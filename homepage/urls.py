from django.contrib import admin
from django.urls import path
import myapp.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.index, name="home"),
    path('index/', myapp.views.index, name="index"),
    path('map/', myapp.views.map, name="map"),
    path('newMap/', myapp.views.newMap, name="newMap"),
    path('detailMap/<int:cat_id>/', myapp.views.detailMap, name="detailMap"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 

from places.views import show_main, get_place_details
# from wtgsite import settings

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name='main'),
    path('places/<int:place_id>/', get_place_details, name='places'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
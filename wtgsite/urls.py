
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places.views import get_place_details, show_main

# from wtgsite import settings




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', show_main, name='main'),
    path('tinymce/', include('tinymce.urls')),
    path('places/<int:place_id>/', get_place_details, name='places'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('feed.urls')),
    path('accounts/', include('accounts.urls')),
    path('events/', include('events.urls')),
    path('interactions/', include('interactions.urls')),
]

# Adicione isso apenas durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
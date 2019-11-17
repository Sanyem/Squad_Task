from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('UserAuth.urls', namespace='UserAuth')),
    url(r'^game/', include('game.urls', namespace='game')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .swagger_urls import urlpatterns as swagger_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include("accounts.urls")),
    path('category/', include("category.urls")),
    path('announcement/', include("announcements.urls")),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += swagger_url
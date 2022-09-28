from django.urls import path
from .views import AnnouncementViewSet
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('posts', AnnouncementViewSet.as_view(), basename='posts')

urlpatterns = [
    path('posts/', AnnouncementViewSet.as_view(), basename='posts'),
]


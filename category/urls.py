from django.urls import path
from . import views


urlpatterns = [
    path('categories/', views.CreateCategoryAPIView.as_view()),
    path('categories-list/', views.CategoryListAPIView.as_view()),
    path('categories-rud/<int:pk>/', views.CategoryRUDAPIView.as_view()),

]
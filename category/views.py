
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from category.models import Category
from category.permissions import ISuperUserOrReadOnly
from category.serializers import CategorySerializer

# Create your views here.

class CreateCategoryAPIView(CreateAPIView):

    permission_classes = [IsAuthenticated, ISuperUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryListAPIView(ListAPIView):
    permission_classes = [ISuperUserOrReadOnly]
    # queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = Category.objects.filter(sub_category=None)
        return queryset

class CategoryRUDAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ISuperUserOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




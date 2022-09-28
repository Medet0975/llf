from django.db import models
from django.conf import settings
from category.models import Category

TYPE_POSTS = (
    (1, "New"),
    (2, "Used"),
)
class Announcement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    type_post = models.IntegerField(choices=TYPE_POSTS, default=1)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

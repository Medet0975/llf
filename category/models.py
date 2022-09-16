from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        if self.sub_category:
            return f"{self.title} --> {self.sub_category}"
        return self.title


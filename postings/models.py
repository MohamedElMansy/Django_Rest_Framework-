from django.db import models
from django.conf import settings

# Create your models here.
class BlogPost(models.Model):
    user =models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    title =models.CharField(max_length=120)
    content=models.CharField(max_length=120)

    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User
 
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=100, unique=True,)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name="blog_title")
    updated_on = models.DateTimeField(auto_now= True)
    body = models.TextField(unique=True)
    description = models.CharField(max_length=200, default="NO DESCRIPTION AVAILABLE")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    # https://docs.djangoproject.com/en/3.1/ref/models/options/
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


from django.db import models

class Post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)  # Fixed: Use CharField for author name
    created_t = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
# Create your models here.

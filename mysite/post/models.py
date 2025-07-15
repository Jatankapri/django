from django.db import models
class post(models.Model):
    """
    Model representing a blog post.
    """
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
       db_table = 'posts'

    def __str__(self):
        return self.title
# Create your models here.

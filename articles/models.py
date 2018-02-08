from django.db import models

# Create your models here.
class Article(models.Model):  # Inheriting basic functionaliites
    # Add in the different fields that you want to store.
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add later
    # thumbnail
    author = models.CharField(max_length=100, default='Me')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + "..."

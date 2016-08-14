from django.db import models
from django.utils import timezone
# Create your models here.



class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateField(default=timezone.now)
    published_at = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish():
        self.published_at = timezone.now()
        self.save()

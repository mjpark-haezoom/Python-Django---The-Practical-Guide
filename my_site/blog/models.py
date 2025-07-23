from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from datetime import date

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.full_name()
    
class Tag(models.Model):
    caption = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name="posts")
    excerpt = models.CharField(max_length=1000)
    content = models.CharField(max_length=1000000)
    image = models.CharField(max_length=50)
    date = models.DateField(default=date.today)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    related_tags = models.ManyToManyField(Tag)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
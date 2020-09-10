from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор публікації')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст пубілкації')
    published = models.DateTimeField(
        default=timezone.now, verbose_name='Час публікації')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250, unique_for_date='published')
    tags = TaggableManager()
    image = models.ImageField(upload_to='img', default='img/atom_256.png')

    class Meta:
        ordering = ['-published', ]

    def __str__(self):
        return self.title

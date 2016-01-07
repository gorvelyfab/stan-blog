from django.db import models


class Tag(models.Model):
    name = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Post(models.Model):
    name = models.CharField('title', max_length=255)
    slug = models.SlugField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']

from django.db import models


class Category(models.Model):
    name = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'


class Work(models.Model):
    name = models.CharField('title', max_length=255)
    slug = models.SlugField('slug', max_length=255)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    client_name = models.CharField('client', max_length=255)
    client_url = models.URLField()

    categories = models.ManyToManyField('Category')

    def __str__(self):
        return self.name


class WorkPicture(models.Model):
    src = models.ImageField()
    work = models.ForeignKey('work', on_delete=models.CASCADE)

    def __str__(self):
        return self.src.url

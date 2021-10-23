from django.db import models
import PIL


class Project(models.Model):
    Image = models.ImageField()
    Name = models.CharField(max_length=100, unique=True)
    Content = models.TextField(max_length=40000, blank=True, null=True)
    Current = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.Name


class Blog(models.Model):
    title = models.CharField(max_length=560)
    image1 = models.ImageField(blank=True, default=None)
    image2 = models.ImageField(blank=True, default=None)
    content = models.TextField(max_length=2000)
    by = models.CharField(max_length=560, null=True)

    def __str__(self) -> str:
        return self.title

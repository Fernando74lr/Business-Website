from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date and time of creation")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date and time of last change")

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="Name")
    content = models.TextField(verbose_name="Content")
    published = models.DateTimeField(verbose_name="Date of creation", default=now)
    image = models.ImageField(verbose_name="Image", upload_to="blog", null=True, blank=True)
    author = models.ForeignKey(User, verbose_name="Auth", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categories", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date and time of creation")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date and time of last change")

    class Meta:
        verbose_name = "entry"
        verbose_name_plural = "entries"
        ordering = ["-created"]

    def __str__(self):
        return self.title
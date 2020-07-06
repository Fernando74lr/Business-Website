from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, blank=False, verbose_name="Title")
    subtitle = models.CharField(max_length=200, blank=False, verbose_name="Subtitle")
    content = models.TextField(blank=False, verbose_name="Content")
    image = models.ImageField(blank=False, upload_to='services', verbose_name="Image")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Date and time of creation")
    updated = models.DateTimeField(auto_now=True, verbose_name="Date and time of last change")

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ["-created"]

    def __str__(self):
        return self.title
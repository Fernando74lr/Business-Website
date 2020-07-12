from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name="Key name",max_length=100, unique=True)
    name = models.CharField(verbose_name="Social Networks", max_length=200)
    url = models.CharField(verbose_name="Link", max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')
    updated = models.DateTimeField(auto_now=True, verbose_name='Date of last modification')

    class Meta:
        verbose_name = 'link'
        verbose_name_plural = 'links'
        ordering = ['name']

    def __str__(self):
        return self.name
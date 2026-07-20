from django.db import models
from django.utils.text import slugify


class Destination(models.Model):

    name = models.CharField(max_length=150)

    slug = models.SlugField(unique=True, blank=True)

    country = models.CharField(max_length=100)

    description = models.TextField()

    best_season = models.CharField(max_length=100)

    estimated_budget = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    image = models.ImageField(
        upload_to='destinations/'
    )

    attractions = models.TextField()

    activities = models.TextField()

    is_featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ['name']

        verbose_name = "Destination"

        verbose_name_plural = "Destinations"

    def save(self,*args,**kwargs):

        if not self.slug:

            self.slug = slugify(self.name)

        super().save(*args,**kwargs)

    def __str__(self):

        return self.name
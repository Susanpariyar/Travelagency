from django.db import models
from django.utils.text import slugify
from destinations.models import Destination


class TourPackage(models.Model):

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Hard', 'Hard'),
    ]

    PACKAGE_TYPE_CHOICES = [
        ('Adventure', 'Adventure'),
        ('Family', 'Family'),
        ('Honeymoon', 'Honeymoon'),
        ('Luxury', 'Luxury'),
        ('Wildlife', 'Wildlife'),
        ('Cultural', 'Cultural'),
        ('Trekking', 'Trekking'),
    ]

    destination = models.ForeignKey(
        Destination,
        on_delete=models.CASCADE,
        related_name='tour_packages'
    )

    name = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    package_type = models.CharField(
        max_length=20,
        choices=PACKAGE_TYPE_CHOICES,
        default='Adventure'
    )

    short_description = models.CharField(max_length=255)

    description = models.TextField()

    duration = models.PositiveIntegerField(
        help_text="Duration in days"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    discount_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )

    max_group_size = models.PositiveIntegerField()

    available_slots = models.PositiveIntegerField(default=20)

    difficulty = models.CharField(
        max_length=20,
        choices=DIFFICULTY_CHOICES
    )

    accommodation = models.CharField(max_length=200)

    transportation = models.CharField(max_length=200)

    departure_location = models.CharField(max_length=150)

    meals_included = models.BooleanField(default=True)

    featured_image = models.ImageField(
        upload_to='packages/'
    )

    

    is_featured = models.BooleanField(default=False)

    is_available = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Tour Package"
        verbose_name_plural = "Tour Packages"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
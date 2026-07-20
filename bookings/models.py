from django.db import models
from django.conf import settings
from packages.models import TourPackage
from decimal import Decimal
from datetime import date


class Booking(models.Model):

    BOOKING_STATUS = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Refunded', 'Refunded'),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    package = models.ForeignKey(
        TourPackage,
        on_delete=models.CASCADE,
        related_name='bookings'
    )

    booking_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    travel_date = models.DateField()

    travelers = models.PositiveIntegerField(default=1)

    contact_phone = models.CharField(max_length=20)

    emergency_contact = models.CharField(
        max_length=100,
        blank=True
    )

    special_requests = models.TextField(
        blank=True
    )

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        editable=False
    )

    booking_status = models.CharField(
        max_length=20,
        choices=BOOKING_STATUS,
        default='Pending'
    )

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Booking"
        verbose_name_plural = "Bookings"

    def save(self, *args, **kwargs):

        # Generate Booking ID
        if not self.booking_id:
            today = date.today().strftime("%Y%m%d")
            last_booking = Booking.objects.order_by('id').last()

            if last_booking:
                number = last_booking.id + 1
            else:
                number = 1

            self.booking_id = f"BK-{today}-{number:04d}"

        # Calculate Total Price
        self.total_price = (
            Decimal(self.travelers) * self.package.price
        )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.booking_id
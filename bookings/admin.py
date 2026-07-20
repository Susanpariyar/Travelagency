from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'booking_id',
        'user',
        'package',
        'travel_date',
        'travelers',
        'total_price',
        'booking_status',
        'payment_status',
    )

    list_filter = (
        'booking_status',
        'payment_status',
        'travel_date',
        'created_at',
    )

    search_fields = (
        'booking_id',
        'user__username',
        'user__email',
        'package__name',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'booking_id',
        'total_price',
        'created_at',
        'updated_at',
    )

    fieldsets = (

        ("Booking Information", {
            'fields': (
                'booking_id',
                'user',
                'package',
                'travel_date',
                'travelers',
            )
        }),

        ("Contact Details", {
            'fields': (
                'contact_phone',
                'emergency_contact',
                'special_requests',
            )
        }),

        ("Status", {
            'fields': (
                'booking_status',
                'payment_status',
                'total_price',
            )
        }),

        ("Dates", {
            'fields': (
                'created_at',
                'updated_at',
            )
        }),
    )
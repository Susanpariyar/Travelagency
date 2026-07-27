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
        'created_at',
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
        'user__first_name',
        'user__email',
        'package__name',
    )

    ordering = (
        '-created_at',
    )

    list_per_page = 20

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

    actions = (
        'mark_as_confirmed',
        'mark_as_completed',
        'mark_as_paid',
        'mark_as_refunded',
    )

    @admin.action(description="Mark selected bookings as Confirmed")
    def mark_as_confirmed(self, request, queryset):
        queryset.update(booking_status="Confirmed")

    @admin.action(description="Mark selected bookings as Completed")
    def mark_as_completed(self, request, queryset):
        queryset.update(booking_status="Completed")

    @admin.action(description="Mark selected bookings as Paid")
    def mark_as_paid(self, request, queryset):
        queryset.update(payment_status="Paid")

    @admin.action(description="Mark selected bookings as Refunded")
    def mark_as_refunded(self, request, queryset):
        queryset.update(payment_status="Refunded")
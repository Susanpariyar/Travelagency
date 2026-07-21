from django.contrib import admin
from .models import TourPackage


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'destination',
        'package_type',
        'price',
        'discount_price',
        'duration',
        'difficulty',
        'available_slots',
        'is_featured',
        'is_available',
    )

    list_filter = (
        'destination',
        'package_type',
        'difficulty',
        'is_featured',
        'is_available',
    )

    search_fields = (
        'name',
        'destination__name',
        'departure_location',
    )

    list_editable = (
        'price',
        'discount_price',
        'is_featured',
        'is_available',
    )

    prepopulated_fields = {
        'slug': ('name',)
    }

    ordering = ('name',)

    save_as = True
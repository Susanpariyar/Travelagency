from django.contrib import admin

from .models import Destination


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'country',
        'best_season',
        'is_featured'
    )

    list_filter = (
        'country',
        'is_featured'
    )

    search_fields = (
        'name',
        'country'
    )

    prepopulated_fields = {
        'slug': ('name',)
    }
from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "package",
        "created_at",
    )

    search_fields = (
        "user__username",
        "package__name",
    )

    list_filter = (
        "created_at",
    )
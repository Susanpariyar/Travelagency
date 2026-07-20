from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'subject',
        'status',
        'created_at',
    )

    list_filter = (
        'is_read',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'subject',
    )

    list_editable = ()

    ordering = (
        '-created_at',
    )

    actions = [
        'mark_as_read',
        'mark_as_unread',
    ]


    def change_view(self, request, object_id, form_url='', extra_context=None):

        message = ContactMessage.objects.get(pk=object_id)

        if not message.is_read:
            message.is_read = True
            message.save()

        return super().change_view(
            request,
            object_id,
            form_url,
            extra_context
    )




    @admin.display(description="Status")
    def status(self, obj):
        if obj.is_read:
            return "🟢 Read"
        return "🔴 New"

    @admin.action(description="Mark selected messages as Read")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Mark selected messages as New")
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
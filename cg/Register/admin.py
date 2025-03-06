
from django.contrib import admin
from .models import rDetails

class rDetailsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_approved=False)

    def approve_registrations(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, 'Selected registrations have been approved.')

    approve_registrations.short_description = 'Approve selected registrations'
    actions = [approve_registrations]

admin.site.register(rDetails, rDetailsAdmin)


# Register your models here.
# admin.py — registers models so they appear in Django's built-in admin panel
# Access at /admin/ after running: python manage.py createsuperuser

from django.contrib import admin
from .models import WaitlistEntry, Review


# ── WAITLIST ADMIN ──────────────────────────────────────────────────────────
@admin.register(WaitlistEntry)
class WaitlistAdmin(admin.ModelAdmin):
    # Columns shown in the list view
    list_display = ['name', 'email', 'city', 'site_rating', 'joined_at']
    # Filters on the right sidebar
    list_filter  = ['city', 'consent_reminders', 'consent_updates']
    # Search bar
    search_fields = ['name', 'email', 'city']
    readonly_fields = ['joined_at']


# ── REVIEW ADMIN ──────────────────────────────────────────────────────────
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ['name', 'city', 'rating', 'approved', 'submitted_at']
    list_filter   = ['approved', 'rating']
    search_fields = ['name', 'comment']
    # Allow toggling approved directly from the list view
    list_editable = ['approved']
    readonly_fields = ['submitted_at']

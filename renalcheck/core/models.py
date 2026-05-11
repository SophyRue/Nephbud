from django.db import models


# models.py — defines the database tables for RenalCheck
# Django automatically creates these as SQLite tables when you run migrations

from django.db import models

# ── WAITLIST MODEL ──────────────────────────────────────────────────────────
# Stores everyone who signs up for early access.
class WaitlistEntry(models.Model):
    name  = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=30, blank=True)
    city  = models.CharField(max_length=100)
    consent_launch    = models.BooleanField(default=False)
    consent_updates   = models.BooleanField(default=False)
    consent_reminders = models.BooleanField(default=False)
    consent_tips      = models.BooleanField(default=False)
    how_heard   = models.CharField(max_length=200, blank=True)
    use_reasons = models.TextField(blank=True)
    concerns    = models.TextField(blank=True)
    site_rating = models.IntegerField(default=0)
    joined_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.email})"

    class Meta:
        ordering = ['-joined_at']
        verbose_name_plural = "Waitlist Entries"


# ── REVIEW MODEL ──────────────────────────────────────────────────────────
# Stores user reviews shown on the homepage.
class Review(models.Model):
    name     = models.CharField(max_length=100)
    city     = models.CharField(max_length=100, blank=True)
    rating   = models.IntegerField()
    comment  = models.TextField()
    approved = models.BooleanField(default=False)  # Only approved reviews show on homepage
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.rating}★"

    class Meta:
        ordering = ['-submitted_at']

# Create your models here.

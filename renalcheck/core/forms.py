# forms.py — Django forms handle validation and HTML field rendering
# Each form maps to a model and controls what users can submit

from django import forms
from .models import WaitlistEntry, Review


# ── WAITLIST FORM ──────────────────────────────────────────────────────────
# Splits across 3 steps in the template but submits as one form
class WaitlistForm(forms.ModelForm):
    class Meta:
        model  = WaitlistEntry
        fields = [
            'name', 'email', 'phone', 'city',
            'consent_launch', 'consent_updates', 'consent_reminders', 'consent_tips',
            'how_heard', 'use_reasons', 'concerns', 'site_rating',
        ]
        widgets = {
            # Add Bootstrap classes and placeholders to each field
            'name':  forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your full name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'you@email.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+234 xxx xxx xxxx (optional)'}),
            'city':  forms.Select(attrs={'class': 'form-select'}),
            'how_heard':   forms.Select(attrs={'class': 'form-select'}),
            'use_reasons': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
                'placeholder': 'e.g. Reminders that actually feel urgent, seeing my progress over time...'}),
            'concerns': forms.Textarea(attrs={'class': 'form-control', 'rows': 3,
                'placeholder': 'e.g. Is my data private? Can it be used by elderly parents?'}),
            'site_rating': forms.HiddenInput(),  # Controlled by star-click JS
        }

    # Override city field to use a dropdown of Nigerian cities
    city = forms.ChoiceField(
        choices=[
            ('', 'Select your state / city'),
            ('Lagos', 'Lagos'),
            ('Abuja (FCT)', 'Abuja (FCT)'),
            ('Benin City (Edo)', 'Benin City (Edo)'),
            ('Port Harcourt (Rivers)', 'Port Harcourt (Rivers)'),
            ('Kano', 'Kano'),
            ('Ibadan (Oyo)', 'Ibadan (Oyo)'),
            ('Enugu', 'Enugu'),
            ('Kaduna', 'Kaduna'),
            ('Other — Nigeria', 'Other — Nigeria'),
            ('Outside Nigeria', 'Outside Nigeria'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    # Override how_heard as a dropdown
    how_heard = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Select'),
            ('Social media', 'Social media (Instagram / Twitter / TikTok)'),
            ('Word of mouth', 'Word of mouth / friend'),
            ('Google search', 'Google search'),
            ('WhatsApp group', 'WhatsApp group'),
            ('Health professional', 'Health professional'),
            ('Other', 'Other'),
        ],
        widget=forms.Select(attrs={'class': 'form-select'})
    )


# ── REVIEW FORM ──────────────────────────────────────────────────────────
class ReviewForm(forms.ModelForm):
    class Meta:
        model  = Review
        fields = ['name', 'city', 'rating', 'comment']
        widgets = {
            'name':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name'}),
            'city':    forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Lagos, Nigeria (optional)'}),
            'rating':  forms.HiddenInput(),  # Set by star-click JS
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4,
                'placeholder': 'Share your experience with this website...'}),
        }

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review
from .forms import WaitlistForm, ReviewForm


# ── HOME PAGE ──────────────────────────────────────────────────────────────
def home(request):
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review_form.save()
            messages.success(request, 'Thank you for your review! It will appear here once approved.')
            return redirect('home')
    else:
        review_form = ReviewForm()

    reviews = Review.objects.filter(approved=True)

    # Features data passed to template — avoids hardcoding in HTML
    features = [
        ('🎯', 'Personalised risk scoring', 'Your risk score is built from your specific profile — not a generic calculator. Age, BMI, blood pressure, family history, diet, and more are all factored in individually.', 'Assessment engine', 'green'),
        ('⏰', 'Intelligent nudge reminders', "If you haven't checked in, RenalCheck sends a personalised message referencing your specific risk profile — not a generic push notification.", 'Behavioral psychology', 'amber'),
        ('📈', 'Progress tracking', 'Your risk score is yours to improve. Track how lifestyle changes — hydration, diet, exercise — actually move your number over time.', 'Longitudinal health data', 'green'),
        ('🏥', 'Doctor referral guidance', "For moderate and high-risk profiles, RenalCheck tells you exactly what tests to request and what to say when you get to the doctor.", 'Clinical pathway support', 'red'),
        ('🔒', 'Private by design', 'Your health data is sensitive. We collect only what we need, and your data is never sold to third parties.', 'Data privacy', 'green'),
        ('🌍', 'Built for Nigeria', 'Risk factors, dietary patterns, and health literacy are different here. RenalCheck is designed with the Nigerian context at its core.', 'Africa-first health tech', 'amber'),
    ]

    # FAQ data — question/answer pairs
    faqs = [
        ('Is RenalCheck a medical diagnostic tool?',
         'No — and we are very clear about this. RenalCheck is a lifestyle-based risk screening tool. It uses clinically-informed risk factors to give you an estimate of your kidney health risk, but it cannot diagnose CKD or any other condition. Only laboratory tests and a doctor\'s examination can do that. We are designed to be the prompt that gets you to the doctor — not the replacement for one.'),
        ('What does the reminder feature actually look like?',
         "RenalCheck uses behaviourally-informed nudge messaging. When you haven't checked in for a set period, the app sends a personalised reminder — not a generic notification. The message references your specific risk profile and communicates the cost of inactivity in real terms. You can control the frequency and channel in your settings."),
        ('Is my health data private and secure?',
         'Yes. RenalCheck is built on data minimisation principles — we only collect what is necessary to generate your risk profile. Your health data is never sold, shared with advertisers, or passed to third parties. You own your data and can request deletion at any time.'),
        ('When will the full app launch?',
         'We are currently in development with a Nigeria-first launch planned. Joining the waitlist puts you in the first cohort to receive access. We will also run a beta testing program — waitlist members will be the first invited.'),
        ('Will RenalCheck be free?',
         'The core risk assessment will always be free. Early waitlist members will receive extended free access to premium features. We will have a freemium model — free for essential screening, with optional paid features for advanced tracking and personalised health coaching.'),
        ('Who is behind RenalCheck?',
         'RenalCheck is being built by a Nigerian founder with a background in health technology, data analysis, and digital product development. The product is designed specifically for the Nigerian and African health context — not adapted from a Western tool.'),
    ]

    return render(request, 'core/home.html', {
        'review_form': review_form,
        'reviews': reviews,
        'features': features,
        'faqs': faqs,
    })


# ── WAITLIST PAGE ──────────────────────────────────────────────────────────
def waitlist(request):
    if request.method == 'POST':
        form = WaitlistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('waitlist_success')
    else:
        form = WaitlistForm()
    return render(request, 'core/waitlist.html', {'form': form})


def waitlist_success(request):
    return render(request, 'core/waitlist_success.html')


# ── ASSESSMENT PAGE ──────────────────────────────────────────────────────
def assessment(request):
    return render(request, 'core/assessment.html')

# Create your views here.

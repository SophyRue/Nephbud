# urls.py (app-level) — maps URL paths to view functions
# This file belongs to the core app

from django.urls import path
from . import views

# Each path() connects a URL to a view function
# name= lets templates reference URLs with {% url 'name' %} instead of hardcoding paths
urlpatterns = [
    path('',                views.home,             name='home'),
    path('waitlist/',       views.waitlist,         name='waitlist'),
    path('waitlist/done/',  views.waitlist_success, name='waitlist_success'),
    path('assessment/',     views.assessment,       name='assessment'),
]

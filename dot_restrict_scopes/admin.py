"""
Django admin configuration for the dot-restrict-scopes package.
"""

from django.contrib import admin
from django.contrib.admin.sites import NotRegistered
from oauth2_provider.admin import ApplicationAdmin

from .forms import RestrictedApplicationForm
from .models import RestrictedApplication

# The restricted application is registered by Django OAuth Toolkit, but we want
# to provide our own admin that uses our form
try:
    admin.site.unregister(RestrictedApplication)
except NotRegistered:
    pass


@admin.register(RestrictedApplication)
class RestrictedApplicationAdmin(ApplicationAdmin):
    form = RestrictedApplicationForm

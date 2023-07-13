# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Organisation


@admin.register(Organisation)
class OrganisationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'organisation_name', 'organisation_domain')
    list_filter = ('user',)

# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Label, Detection


@admin.register(Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Detection)
class DetectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'labels', 'x', 'y', 'uni_id')
    list_filter = ('labels',)

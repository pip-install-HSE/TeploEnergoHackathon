from django.contrib import admin

from .models import StaticAnalytics


@admin.register(StaticAnalytics)
class StaticAnalyticsAdmin(admin.ModelAdmin):
    pass

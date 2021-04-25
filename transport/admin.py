from django.contrib import admin

from .models import StaticAnalytics, AnalyticsResult


@admin.register(StaticAnalytics)
class StaticAnalyticsAdmin(admin.ModelAdmin):
    pass


@admin.register(AnalyticsResult)
class AnalyticsResultAdmin(admin.ModelAdmin):
    pass

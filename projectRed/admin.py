from django.contrib import admin
from .models import HamperRequest


@admin.register(HamperRequest)
class HamperRequestAdmin(admin.ModelAdmin):
    list_display = ("student_name", "family_size", "priority", "created_at")
    list_filter = ("priority",)
    search_fields = ("student_name", "comments")

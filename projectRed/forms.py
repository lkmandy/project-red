from django import forms
from .models import HamperRequest

class HamperRequestForm(forms.ModelForm):
    class Meta:
        model = HamperRequest
        fields = ["student_name", "family_size", "priority", "comments"]

from django import forms
from .models import FeedbackForm


class TextForm(forms.ModelForm):
    class Meta:
        model = FeedbackForm
        fields = ['name', 'email', 'text']
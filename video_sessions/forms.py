from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('author', 'num_video_preferido', 'text')

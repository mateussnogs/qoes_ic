from django import forms

from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('nome', 'num_video_preferido', 'justificativa')

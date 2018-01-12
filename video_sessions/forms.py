from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('incomodo', 'interesse1', 'interesse2', 'num_video_preferido', 'justificativa')
        labels = {
            'num_video_preferido': _('Qual foi o seu vídeo preferido?(1 ou 2)'),
            'incomodo': _("Em uma escala de 1 a 10, qual foi o seu incômodo com as interrupções?"),
            'interesse1': _("Em uma escala de 1 a 10 qual foi seu interesse pelo conteúdo do vídeo 1?"),
            'interesse2': _("E pelo vídeo 2?"),
            'justificativa': _("Por que você preferiu esse vídeo?")
        }

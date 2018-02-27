from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('incomodo', 'interesse1', 'interesse2', 'num_video_preferido', 'justificativa', 'comment', 'email')
        labels = {
            'num_video_preferido': _('Qual foi o seu vídeo preferido?'),
            'incomodo': _("Em uma escala de 1 a 10 qual foi o seu incômodo com as interrupções?"),
            'interesse1': _("Em uma escala de 1 a 10 qual foi seu interesse pelo conteúdo do vídeo 1?"),
            'interesse2': _("E pelo vídeo 2?"),
            'justificativa': _("Por quê você preferiu esse vídeo?"),
            'comment': _("Comentários sobre a sessão"),
            'email': _("E-mail:"),
        }
        widgets = {
          'comment': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'justificativa': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }

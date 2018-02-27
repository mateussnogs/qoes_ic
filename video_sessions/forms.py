from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Feedback, StressFeedback


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('incomodo', 'interesse1', 'interesse2', 'num_video_preferido', 'justificativa', 'comment', 'email')
        labels = {
            'num_video_preferido': _('Qual foi o seu vídeo preferido?'),
            'incomodo': _("Em uma escala de 1 a 10 qual foi o seu incômodo com as interrupções no vídeo de pior qualidade?"),
            'interesse1': _("Em uma escala de 1 a 10 qual foi seu interesse pelo conteúdo do vídeo 1?"),
            'interesse2': _("E pelo vídeo 2?"),
            'justificativa': _("Por quê você preferiu esse vídeo?"),
            'comment': _("Comentários sobre a sessão"),
            'email': _("Seu e-mail: "),
        }
        widgets = {
          'comment': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'justificativa': forms.Textarea(attrs={'rows':4, 'cols':15}),
        }

class StressForm(forms.ModelForm):

    class Meta:
        model = StressFeedback
        fields = ('estresse', 'justificativa', 'rebuff_feedback', 'recommend_feedback', 'email')
        labels = {
            'estresse': _("Em uma escala de 1 a 10, o quanto os distúrbios de qualidade do vídeo incomodaram?"),
            'justificativa': _("Impressões dessa sessão"),
            'rebuff_feedback': _("O que você iria preferir: esperar 5 segundos e assistir o vídeo estável em HD, ou assistir \
             de imediato o vídeo deturpado(o primeiro)?"),
            'recommend_feedback': _("Pensando em vídeos aleatoriamente, você acha que iria preferir um outro da mesma categoria, \
            porém completamente estável e com a qualidade muito boa?"),
            'email': _("Seu e-mail: "),
        }
        widgets = {
          'justificativa': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'rebuff_feedback': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'recommend_feedback': forms.Textarea(attrs={'rows':3, 'cols':15}),
        }

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Feedback, StressFeedback
from django.utils.safestring import mark_safe

STARS = (
    ('0', 0),
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)


class HorizontalRadioSelect(forms.RadioSelect):
    template_name = 'video_sessions/horizontal_select.html'

str_comentario_label = "Comentários sobre a sessão(Opcional). As falhas de qualidade foram muito perceptíveis? \
O tempo dos vídeos foi muito curto para julgá-los? Houve entretenimento durante a sessão?"
class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('interesse1', 'interesse2', 'num_video_preferido', 'justificativa', 'incomodo', 'comment', 'email')
        labels = {
            'num_video_preferido': _('Qual foi o seu vídeo preferido?'),
            'interesse1': _("Em uma escala de 0 a 5 qual é o seu interesse pelo conteúdo/tópico do vídeo 1?"),
            'interesse2': _("E pelo vídeo 2?"),
            'justificativa': _("Por quê você preferiu esse vídeo?"),
            'incomodo': _("Em uma escala de 0 a 5 qual foi o seu incômodo com as interrupções no vídeo de pior qualidade?"),
            'comment': _(str_comentario_label),
            'email': _(""),
        }
        widgets = {
          'comment': forms.Textarea(attrs={'rows':4, 'cols':15}),
          'justificativa': forms.Textarea(attrs={'rows':3, 'cols':15}),
          'incomodo': HorizontalRadioSelect(choices=STARS),
          'interesse1': HorizontalRadioSelect(choices=STARS),
          'interesse2': HorizontalRadioSelect(choices=STARS),
        }

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['justificativa'].required = False
        self.fields['comment'].required = False
        self.fields['email'].widget = forms.HiddenInput()

class StressForm(forms.ModelForm):

    class Meta:
        model = StressFeedback
        fields = ('estresse', 'email')
        labels = {
            'estresse': _("Em uma escala de 1 a 10, qual foi o seu estresse com as falhas de qualidade do primeiro vídeo?"),
            'email': _("Seu e-mail: "),
        }

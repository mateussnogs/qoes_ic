from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Feedback, StressFeedback, Categories
from django.utils.safestring import mark_safe
from django.forms.widgets import SelectMultiple, Select

STARS = (
    ('0', 0),
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
)

STARS_STRESS = (
    ('0', 0),
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
)

FIRST = 1
SECOND = 2
NONE = 0
ESCOLHAS_VIDEO = (
    (FIRST, 'Primeiro'),
    (SECOND, 'Segundo'),
    (NONE, 'Nenhum'),
    ("", "")
)
VIDEO_CHOICES = (
    (FIRST, 'First'),
    (SECOND, 'Second'),
    (NONE, 'None'),
    ("", ""),
)


class HorizontalRadioSelect(forms.RadioSelect):
    template_name = 'video_sessions/horizontal_select.html'

str_comentario_label = "Comentários sobre a sessão(Opcional). Houve entretenimento durante a sessão? Algum outro comentário?"

str_comentario_label_en="Comments about the session (optional): Was there entertainment during the session? Any other comment?"

class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('interesse1', 'interesse2', 'num_video_preferido', 'justificativa', 'incomodo', 'comment', 'email')
        labels = {
            'num_video_preferido': _('Qual foi o seu vídeo preferido, considerando as falhas de qualidade?'),
            'interesse1': _("Em uma escala de 0 a 5 qual é o seu interesse pelo conteúdo do vídeo 1(independentemente das falhas)?"),
            'interesse2': _("E pelo do vídeo 2(independentemente das falhas)?"),
            'justificativa': _("Por quê você preferiu esse vídeo?"),
            'incomodo': _("Em uma escala de 0 a 5 qual foi o seu incômodo com as interrupções no vídeo de pior qualidade?"),
            'comment': _(str_comentario_label),
            'email': _(""),
        }
        widgets = {
          'num_video_preferido': Select(choices=ESCOLHAS_VIDEO),
          'comment': forms.Textarea(attrs={'rows':1, 'cols':15}),
          'justificativa': forms.Textarea(attrs={'rows':1, 'cols':15}),
          'incomodo': HorizontalRadioSelect(choices=STARS),
          'interesse1': HorizontalRadioSelect(choices=STARS, attrs={'size':25}),
          'interesse2': HorizontalRadioSelect(choices=STARS),
        }

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['justificativa'].required = False
        self.fields['comment'].required = False
        self.fields['email'].required = False
        self.fields['email'].widget = forms.HiddenInput()


class StressForm(forms.ModelForm):

    class Meta:
        model = StressFeedback
        fields = ('estresse', 'email')
        labels = {
            'estresse': _("Em uma escala de 0 a 10, qual foi o seu estresse com as falhas de qualidade do primeiro vídeo?"),
            'email': _(""),
        }
        widgets = {
            'estresse': HorizontalRadioSelect(choices=STARS_STRESS),
            #'estresse':forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }

    def __init__(self, *args, **kwargs):
        super(StressForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['email'].widget = forms.HiddenInput()




# ctrl-c ctrl-v para adaptando forms acima para ingles

class FeedbackForm_en(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('interesse1', 'interesse2', 'num_video_preferido', 'justificativa', 'incomodo', 'comment', 'email')
        labels = {
            'num_video_preferido': _('What was your favorite movie considering the flaws?'),
            'interesse1': _("In a scale from 0 to 5, what is your interest by the content of movie 1?"),
            'interesse2': _("And by the content of movie 2?"),
            'justificativa': _("Why did you prefer that movie?"),
            'incomodo': _("In a scale from 0 to 5, how much did you feel impaired by the interruptions in the movie with lower streaming quality?"),
            'comment': _(str_comentario_label_en),
            'email': _(""),
        }
        widgets = {
          'num_video_preferido': Select(choices=VIDEO_CHOICES),
          'comment': forms.Textarea(attrs={'rows':2, 'cols':15}),
          'justificativa': forms.Textarea(attrs={'rows':1, 'cols':15}),
          'incomodo': HorizontalRadioSelect(choices=STARS),
          'interesse1': HorizontalRadioSelect(choices=STARS),
          'interesse2': HorizontalRadioSelect(choices=STARS),
        }

    def __init__(self, *args, **kwargs):
        super(FeedbackForm_en, self).__init__(*args, **kwargs)
        self.fields['justificativa'].required = False
        self.fields['comment'].required = False
        self.fields['email'].required = False
        self.fields['email'].widget = forms.HiddenInput()


class StressForm_en(forms.ModelForm):

    class Meta:
        model = StressFeedback
        fields = ('estresse', 'email')
        labels = {
            'estresse': _("In a scale from 0 to 10, what was your stress level while watching the first movie, with breaks?"),
            'email': _(""),
        }
        widgets = {
            'estresse': HorizontalRadioSelect(choices=STARS_STRESS),
            #'estresse':forms.NumberInput(attrs={'min': 0, 'max': 10}),
        }

    def __init__(self, *args, **kwargs):
        super(StressForm_en, self).__init__(*args, **kwargs)
        self.fields['email'].required = False
        self.fields['email'].widget = forms.HiddenInput()



class CategoriesForm(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('esporte', 'comedia', 'musica', 'documentario', 'animais', 'email')
        labels = {
            'esporte': _("Esportes:"),
            'comedia': _("Comédia: "),
            'musica': _("Música: "),
            'documentario': _("Documentários: "),
            'animais': _("Animais: "),
            'email': _("Email(opcional): "),
        }
        widgets= {
            'esporte': Select(choices=STARS[1:]),
            'comedia': Select(choices=STARS[1:]),
            'musica': Select(choices=STARS[1:]),
            'documentario': Select(choices=STARS[1:]),
            'animais': Select(choices=STARS[1:]),

        }
        def __init__(self, *args, **kwargs):
            super(CategoriesForm, self).__init__(*args, **kwargs)
            self.fields['email'].required = False

class CategoriesForm_en(forms.ModelForm):

    class Meta:
        model = Categories
        fields = ('esporte', 'comedia', 'musica', 'documentario', 'animais', 'email')
        labels = {
            'esporte': _("Sports:"),
            'comedia': _("Comedy: "),
            'musica': _("Music: "),
            'documentario': _("Documentaries: "),
            'animais': _("Animals: "),
            'email': _("Email(optional): "),
        }
        widgets= {
            'esporte': Select(choices=STARS[1:]),
            'comedia': Select(choices=STARS[1:]),
            'musica': Select(choices=STARS[1:]),
            'documentario': Select(choices=STARS[1:]),
            'animais': Select(choices=STARS[1:]),
        }
        def __init__(self, *args, **kwargs):
            super(CategoriesForm, self).__init__(*args, **kwargs)
            self.fields['email'].required = False

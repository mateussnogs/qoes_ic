from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Feedback(models.Model):
    incomodo = models.IntegerField(validators=[MinValueValidator(0),
                                        MaxValueValidator(10)])

    # incomodo = models.CharField(max_length=1, choices=STARS)

    interesse1 = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    interesse2 = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    num_sessao = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(10)])

    num_video_preferido = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(2)])

    justificativa = models.TextField(default="")

    comment = models.TextField(default="")

    email = models.CharField(max_length=40, default="", blank=True, null=True)

    english = models.NullBooleanField(default=False)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    session_id = models.CharField (
        'Chave sessão', max_length=40, default="", null = True, blank=True,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.num_video_preferido)


class StressFeedback(models.Model):
    estresse = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])

    num_sessao = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(10)])

    justificativa = models.TextField(default='', blank=True, null=True)

    rebuff_feedback = models.TextField(default='', blank=True, null=True)

    recommend_feedback = models.TextField(default='', blank=True, null=True)

    email = models.CharField(max_length=40, default="", blank=True, null=True)

    english = models.NullBooleanField(default=False)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    session_id = models.CharField (
        'Chave sessão', max_length=40, default="", null=True, blank=True,
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.estresse)

class Categories(models.Model):
    comedia = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)], null = True)
    esporte = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)], null = True)
    documentario = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)], null = True)
    musica = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)], null = True)

    animais = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(5)], null = True)

    email = models.CharField(max_length=40, default="", blank=True, null=True)

    english = models.NullBooleanField(default=False)

    session_id = models.CharField (
        'Chave sessão', max_length=40, default="", null = True, blank=True,
    )

    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return "Categoria"

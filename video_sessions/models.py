from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Feedback(models.Model):
    incomodo = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    interesse1 = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    interesse2 = models.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(10)])
    num_sessao = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(10)])
    FIRST = 1
    SECOND = 2
    VIDEO_CHOICES = (
        (FIRST, 'Primeiro'),
        (SECOND, 'Segundo'),
    )
    num_video_preferido = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(2)], choices=VIDEO_CHOICES)

    justificativa = models.TextField()

    comment = models.TextField(default="")

    email = models.CharField(max_length=40, default="")

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

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

    justificativa = models.TextField()

    rebuff_feedback = models.TextField()

    recommend_feedback = models.TextField()

    email = models.CharField(max_length=40, default="")

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.estresse)

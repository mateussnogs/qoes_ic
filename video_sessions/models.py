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
    num_video_preferido = models.IntegerField(validators=[MinValueValidator(1),
                                       MaxValueValidator(2)])
    justificativa = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.num_video_preferido)

from django.db import models
from django.utils import timezone
# Create your models here.


class Feedback(models.Model):
    incomodo = models.IntegerField()
    interesse1 = models.IntegerField()
    interesse2 = models.IntegerField()
    num_sessao = models.IntegerField()
    num_video_preferido = models.IntegerField()
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

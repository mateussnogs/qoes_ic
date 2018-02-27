# Generated by Django 2.0.1 on 2018-02-27 18:19

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video_sessions', '0014_auto_20180227_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='StressFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estresse', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('num_sessao', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('justificativa', models.TextField()),
                ('rebuff_feedback', models.TextField()),
                ('recommend_feedback', models.TextField()),
                ('email', models.CharField(default='', max_length=40)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]

# Generated by Django 2.0.1 on 2018-06-21 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_sessions', '0021_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='english',
            field=models.NullBooleanField(default=False),
        ),
        migrations.AddField(
            model_name='stressfeedback',
            name='english',
            field=models.NullBooleanField(default=False),
        ),
    ]

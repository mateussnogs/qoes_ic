# Generated by Django 2.0.1 on 2018-06-21 17:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('video_sessions', '0022_auto_20180621_0149'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
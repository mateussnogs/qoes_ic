# Generated by Django 2.0.6 on 2018-08-23 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_sessions', '0030_categories_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='email',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='stressfeedback',
            name='email',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
    ]
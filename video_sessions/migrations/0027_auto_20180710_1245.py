# Generated by Django 2.0.1 on 2018-07-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_sessions', '0026_auto_20180630_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='session_id',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Chave sessão'),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='session_id',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Chave sessão'),
        ),
        migrations.AlterField(
            model_name='stressfeedback',
            name='session_id',
            field=models.CharField(default='', max_length=40, null=True, verbose_name='Chave sessão'),
        ),
    ]
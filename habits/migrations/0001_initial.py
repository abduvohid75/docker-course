# Generated by Django 3.2.20 on 2023-10-12 17:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='Место')),
                ('time', models.DateTimeField(verbose_name='Время')),
                ('action', models.CharField(max_length=100, verbose_name='Действие')),
                ('nicehab', models.CharField(blank=True, max_length=150, null=True, verbose_name='Признак приятной привычки')),
                ('relhab', models.CharField(blank=True, max_length=150, null=True, verbose_name='Связанная привычка')),
                ('reward', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вознаграждение')),
                ('time_to_act', models.IntegerField(verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
            },
        ),
    ]

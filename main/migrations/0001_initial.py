# Generated by Django 4.0.6 on 2022-09-16 03:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='exercise', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('sets', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('reps', models.CharField(max_length=15)),
                ('weight', models.CharField(max_length=15)),
                ('comment', models.TextField(default='None', max_length=300)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.exercise')),
            ],
        ),
    ]

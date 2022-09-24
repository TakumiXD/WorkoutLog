# Generated by Django 4.0.6 on 2022-09-18 23:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_workout_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='reps',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='sets',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='workout',
            name='weight',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(9999), django.core.validators.MinValueValidator(1)]),
        ),
    ]

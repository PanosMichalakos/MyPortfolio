# Generated by Django 4.0.2 on 2022-03-29 14:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='proficiency',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
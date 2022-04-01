from msilib.schema import Class
from unicodedata import decimal
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime

# Create your models here.


class EducationEntry(models.Model):
    title = models.CharField(max_length=255)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    institution = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class ExperienceEntry(models.Model):
    position = models.CharField(max_length=255)
    start_date = models.DateField(
        auto_now=False, auto_now_add=False)
    end_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True)
    company = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.position


class Skill(models.Model):
    name = models.CharField(max_length=50)
    percentage_validators = [MinValueValidator(0), MaxValueValidator(100)]
    proficiency = models.IntegerField(
        null=True, blank=True, validators=percentage_validators)
    is_programming = models.BooleanField()

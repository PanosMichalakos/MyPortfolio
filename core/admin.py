from django.contrib import admin
from .models import ExperienceEntry, EducationEntry, Skill

# Register your models here.
# admin.site.register(ExperienceEntry)
# admin.site.register(EducationEntry)


@admin.register(EducationEntry)
class EducationEntryAdmin(admin.ModelAdmin):
    list_display = ("title", "institution")

    class Meta:
        ordering = ("start_date")


@admin.register(ExperienceEntry)
class ExperienceEntryAdmin(admin.ModelAdmin):
    list_display = ("position", "company")

    class Meta:
        ordering = ("start_date")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency", "is_programming")

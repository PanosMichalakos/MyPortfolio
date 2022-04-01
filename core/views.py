from django.shortcuts import render
from django.views.generic import TemplateView
from .models import EducationEntry, ExperienceEntry, Skill


# Create your views here.


def index(request):
    education_entries = EducationEntry.objects.all()
    experience_entries = ExperienceEntry.objects.order_by('-start_date')
    generic_skills = Skill.objects.filter(is_programming=False).order_by('-proficiency')
    programming_skills = Skill.objects.filter(is_programming=True).order_by('-proficiency')
    context = {
        'education': education_entries,
        'experience': experience_entries,
        'generic_skills': generic_skills,
        'programming_skills': programming_skills
    }
    return render(request, 'index.html', context)

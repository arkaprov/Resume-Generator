from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import ResumeForm
from .models import Profile
def home(request):
    if request.method =='POST':
        name= request.POST.get('name')
        education=(request.POST.get('education'))
        achievements = (request.POST.get('achievements'))
        skills = (request.POST.get('skills'))
        workExp = (request.POST.get('workExp'))
        email = (request.POST.get('email'))
        phone = (request.POST.get('phone'))
        projects = (request.POST.get('projects'))
        profile=Profile(
            name=name,
            education=education,
            achievements=achievements,
            skills=skills,
            workExp=workExp,
            email=email,
            phone=phone,
            projects=projects
        )
        profile.save()
        return render(request, "profile.html", context={'profile':profile})

    form=ResumeForm()
    context={"form":form}
    return render(request,"resume_form.html",context=context)


def index(request):
    return HttpResponse("You're at the resume generator.")
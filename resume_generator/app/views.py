from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .forms import ResumeForm
def home(request):
    if request.method =='POST':
        print(request.POST.get('name'))
        print(request.POST.get('achievements'))
    form=ResumeForm()
    context={"form":form}
    return render(request,"resume_form.html",context=context)


def index(request):
    return HttpResponse("You're at the resume generator.")
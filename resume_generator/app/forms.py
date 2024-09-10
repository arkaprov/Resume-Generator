from django import forms
from .models import Profile
class ResumeForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields="__all__"
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
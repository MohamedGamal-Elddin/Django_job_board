from django import forms 
from .models import Apply,Job

 

class ApllyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','cv','website','cover_letter']

class post_jobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        exclude=('owner','slug')


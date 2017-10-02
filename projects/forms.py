from django import forms

from .models import project, teams
from pagedown.widgets import PagedownWidget

class projectForm(forms.ModelForm):
    project_description = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = project
        fields = [
            'team_name',
            'project_title',
            'project_description',
            'source_code',
            'webpage',
            'image',
            'developing_or_developed',
            'key',
        ]

class teamsForm(forms.ModelForm):
    class Meta:
        model = teams
        fields = [
            'Team_Name',
            'Name',
            'Facebook_Profile_Link',
            'Github_Profile_Link',
            'Linkedin_Profile_Link',
            'Image',
            'Key',
        ]

class edit(forms.ModelForm):
    class Meta:
        model = project
        fields = [
           'key',
        ]

class editForm(forms.ModelForm):
    project_description = forms.CharField(widget=PagedownWidget)
    class Meta:
        model = project
        fields = [
            'team_name',
            'project_title',
            'project_description',
            'source_code',
            'webpage',
            'image',
            'developing_or_developed',
        ]
from django import forms

from app.models import *
class TopicForm(forms.Form):
    topicname=forms.CharField(max_length=100)



class WebpageForm(forms.Form):
    topicname=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(max_length=100)
    url=forms.URLField()


class Accessrecordform(forms.Form):
    name=forms.ModelChoiceField(queryset=Webpage.objects.all())
    author=forms.CharField(max_length=100)
    date=forms.DateField()

    
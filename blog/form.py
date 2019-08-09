from django import forms
from .models import Blog




class BlogPost(forms.ModelForm):
    blog_title = forms.CharField(required = False, widget = forms.TextInput(
    attrs={
    'name':'title',
    'placeholder':'Enter the title',
    'class':'form-control',
    'type':'text',
    }
    ))
    blog_subtitle = forms.CharField(required = False, widget = forms.TextInput(
    attrs={
    'name':'subtitle',
    'placeholder':'Enter the subtitle',
    'class':'form-control',
    'type':'text',
    }
    ))
    blog_contents = forms.CharField(required = False, widget = forms.Textarea(
    attrs={
    'name':'content',
    'placeholder':'Enter the content',
    'class':'form-control',
    'type':'text',
    }
    ))

    class Meta:
        model = Blog
        fields = ["blog_title", "blog_subtitle", "blog_contents"]

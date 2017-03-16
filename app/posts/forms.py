from django import forms

from pagedown.widgets import PagedownWidget
from mediumeditor.widgets import MediumEditorTextarea

from .models import Post


class PostForm(forms.ModelForm):


    content = forms.CharField(widget=MediumEditorTextarea())
    # content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)


    class Meta:
    	model = Post
    	fields = [
        "title",
        "image",
        "content",
        "draft",
        "publish",
    	]

        # widgets = {
        #     'content': MediumEditorTextarea(),
        # }

class RegistrationForm(forms.Form):

    pass
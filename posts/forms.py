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

class CommentForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['content'].label = False
        
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    # parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(widget=forms.Textarea)
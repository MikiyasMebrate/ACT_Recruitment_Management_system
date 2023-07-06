from django import forms
from  .models import Comment

class CommentForm(forms.ModelForm):
    name = forms.CharField(max_length=40, error_messages={'required' : 'Title can not be empty'})
    email = forms.EmailField(widget=forms.TextInput(), error_messages={'required' : 'Email can not be empty'})
    comment = forms.CharField(widget=forms.TextInput(), error_messages={'required': 'Comment can not be empty'})
    
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment']

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError(' Enter a valid name.')
        return name


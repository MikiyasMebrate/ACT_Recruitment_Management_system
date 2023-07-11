from django import forms
from .models import Candidate, Skill, Education, Experience
from datetime import date
class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if not first_name or len(first_name) < 2:
            raise forms.ValidationError('Enter a Valid Name')
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if not last_name or  len(last_name) < 2:
            raise forms.ValidationError('Enter a Valid Name')
        return last_name
    
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        min_date = date(1900, 1,1)
        max_date = date(2007, 1,1)
        if date_of_birth < min_date or date_of_birth > max_date:
            raise forms.ValidationError('Invalid date of Birth')
        return date_of_birth
    
    def clean_photo(self):
        photo = self.cleaned_data['photo']
        max_size_mb = 1
        max_size_bytes = max_size_mb * 1024 * 1024
        
        if not photo:
            return photo
        if photo.size > max_size_bytes:
            raise forms.ValidationError(
            ('The image file size is too large. Please upload an image smaller than 1 MB.'),
            code='invalid_image_size',
            params={'max_size_mb': max_size_mb},
            )
        return photo
    
    def clean_about(self):
        about = self.cleaned_data['about']
        if not about or len(about) < 10:
         raise forms.ValidationError('Enter a Valid Resume')
        return about

        

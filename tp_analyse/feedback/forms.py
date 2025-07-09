from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['author_name', 'comment', 'rating']
        
    def clean_rating(self):
        rating = self.cleaned_data.get('rating')
        if rating < 1 or rating > 5: # type: ignore
            raise forms.ValidationError("La note doit être entre 1 et 5.")
        return rating
        
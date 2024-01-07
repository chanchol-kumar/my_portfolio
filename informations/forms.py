from django import forms
from informations.models import FeedbackModel,ContactModel


class ContactForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = '__all__'



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'accept': 'feedback_images/*'}),  
        }
        labels = {
            'name': 'Your Name',
            'email': 'Your Email',
            'image': 'Upload Image',
            'feedback': 'Your Feedback',
            'rating': 'Rating',
        }
        help_texts = {
            'image': 'Choose an image file (JPEG, PNG, etc.).',
            'rating': 'Select a rating from the options.',
        }

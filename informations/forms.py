from django import forms
from informations.models import FeedbackModel,UserContactModel


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = '__all__'

class UserContactForm(forms.ModelForm):
    class Meta:
        model = UserContactModel
        fields = '__all__'
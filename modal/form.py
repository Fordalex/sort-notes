from django import forms
from .models import Modal

class informationForm(forms.ModelForm):
    class Meta:
        model = Modal
        fields = ('title', 'information')
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
             'information' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
        }
from django import forms
from .models import ModalSection

class informationForm(forms.ModelForm):
    class Meta:
        model = ModalSection
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
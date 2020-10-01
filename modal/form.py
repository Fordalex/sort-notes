from django import forms
from .models import ModalSection, ModalData

class informationForm(forms.ModelForm):
    class Meta:
        model = ModalSection
        fields = ('title', 'information', 'collapse')
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

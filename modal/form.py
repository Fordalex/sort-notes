from django import forms
from .models import ModalSection, ModalData

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

class dataForm(forms.ModelForm):
    class Meta:
        model = ModalData
        fields = ('title', 'data_style', 'data')
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
             'data_style' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
             'data' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
        }
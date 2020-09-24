from django import forms
from .models import Subject, Section, Attribute, DropDown, Item


class subjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ('title', 'information', 'image',)
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
             'image' : forms.FileInput(
                attrs = {
                    'class' : 'container-fluid form-control'
                    }
            ),
        }

class sectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ('title',)
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
        }

class attributeForm(forms.ModelForm):
    class Meta:
        model = Attribute
        fields = ('title',)
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
        }

class dropdownForm(forms.ModelForm):
    class Meta:
        model = DropDown
        fields = ('title',)
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
        }

class itemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'website', 'model')
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
            'website' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'placeholder': 'www.please_copy_link.com',
                    }
            )
        }
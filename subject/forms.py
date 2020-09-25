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
        fields = ('title','icon')
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    }
            ),
             'icon' : forms.TextInput(
                attrs = {
                    'class' : 'container-fluid form-control',
                    'placeholder': 'https://img.icons8.com/cotton/18/000000/create-new--v1.png',
                    }
            ),
        }

class itemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'website', 'modal_boolean')
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
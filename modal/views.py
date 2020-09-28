from django.shortcuts import render, redirect, get_object_or_404
from subject.models import Subject, Item
from .models import ModalSection, ModalData
from .form import informationForm
from .functions import convert_string_into_data_type, format_data_for_database

# Create your views here.
def modal(request, subject_pk, item_pk):
    """
    Display the information of an item from the subject page.
    """
    item = get_object_or_404(Item, pk=item_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)
    quick_buttons = item.modal.all()
    sections = convert_string_into_data_type(item.modal.all())

    context = {
        'item': item,
        'subject': subject,
        'sections': sections,
    }

    return render(request, 'modal/home.html', context)

def add_modal_section(request, subject_pk, item_pk):
    """
    Add a section to the modal information.
    """
    subject = get_object_or_404(Subject, pk=subject_pk)
    item = get_object_or_404(Item, pk=item_pk)

    if request.method == "POST":
        information = informationForm(request.POST)
        print(information)
        if information.is_valid():
            print('working')
            information_form = information.save(commit=False)
            information_form.save()
            item.modal.add(information_form)

            return redirect('modal', subject.id, item.id)

    print('this shouldt be displayed.')

    context = {
         'informationForm': informationForm,
    }

    return render(request, 'modal/add_modal_section.html', context)

def add_data(request, section_pk, item_pk, subject_pk):
    """
    Add data page with muliple forms.
    """
    section = get_object_or_404(ModalSection, pk=section_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)
    item = get_object_or_404(Item, pk=item_pk)

    if request.method == "POST":
        data = format_data_for_database(request)
        ModalData.add_modal_data(request, section, data)
        return redirect('modal', subject.id, item.id)
        
    return render(request, 'modal/add_data.html')

def edit_modal_section(request, pk):
    """
    Edit a modal section.
    """
    modal = get_object_or_404(ModalSection, pk=pk)

    context = {
        'modal': modal,
    }

    return render(request, 'modal/edit_modal_section.html', context)

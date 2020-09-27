from django.shortcuts import render, redirect, get_object_or_404
from subject.models import Subject, Item
from .models import ModalSection
from .form import informationForm
from .functions import convert_string_into_data_type

# Create your views here.
def modal(request, subject_pk, item_pk):

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

def edit_modal_section(request, pk):

    modal = get_object_or_404(ModalSection, pk=pk)

    context = {
        'modal': modal,
    }

    return render(request, 'modal/edit_modal_section.html', context)
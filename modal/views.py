from django.shortcuts import render, redirect, get_object_or_404
from subject.models import Subject, Item
from .models import Modal
from .form import informationForm

# Create your views here.
def modal(request, subject_pk, item_pk):

    item = get_object_or_404(Item, pk=item_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)
    quick_buttons = item.modal.all()

    context = {
        'item': item,
        'subject': subject,
    }

    return render(request, 'modal/home.html', context)

def add_information(request, subject_pk, item_pk):

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

    return render(request, 'modal/add_information.html', context)

def edit_information(request, pk):

    modal = get_object_or_404(Modal, pk=pk)

    context = {
        'modal': modal,
    }

    return render(request, 'modal/edit_information.html', context)
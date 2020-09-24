from django.shortcuts import render, redirect
from .models import Subject, Section, Attribute, DropDown, Item
from .forms import subjectForm, sectionForm, attributeForm, dropdownForm, itemForm

# Create your views here.
def subject(request, pk):

    subject = Subject.objects.get(pk=pk)

    context = {
        'subject': subject
    }

    return render(request, 'subject/subject.html', context)

def edit_subject(request):

    if request.method == "POST":
        form = subjectForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('menu')

    context = {
        'subjectForm': subjectForm
    }

    return render(request, 'subject/edit_subject.html', context)

def edit_section(request, pk):

    subject = Subject.objects.get(pk=pk)

    if request.method == "POST":
        form = sectionForm(request.POST)
        if form.is_valid:
            section = form.save(commit=False)
            section.save()
            subject.section.add(section.id)
            
            return redirect('subject', pk)

    context = {
        'sectionForm': sectionForm,
        'subject': subject,
    }

    return render(request, 'subject/edit_section.html', context)

def edit_attribute(request, pk):

    section = Section.objects.get(pk=pk)

    if request.method == "POST":
        form = attributeForm(request.POST)
        if form.is_valid:
            attribute = form.save(commit=False)
            attribute.save()
            section.attribute.add(attribute.id)
            
            return redirect('menu')

    context = {
        'attributeForm': attributeForm
    }

    return render(request, 'subject/edit_attribute.html', context)

def edit_dropdown(request, pk):

    attribute = Attribute.objects.get(pk=pk)

    if request.method == "POST":
        form = dropdownForm(request.POST)
        if form.is_valid:
            dropdown = form.save(commit=False)
            dropdown.save()
            attribute.dropdown.add(dropdown.id)
            
            return redirect('menu')

    context = {
        'dropdownForm': dropdownForm
    }

    return render(request, 'subject/edit_dropdown.html', context)

def edit_item(request, pk):

    dropdown = DropDown.objects.get(pk=pk)

    if request.method == "POST":
        form = itemForm(request.POST)
        if form.is_valid:
            item = form.save(commit=False)
            item.save()
            dropdown.item.add(item.id)
            
            return redirect('menu')

    context = {
        'itemForm': itemForm
    }

    return render(request, 'subject/edit_item.html', context)
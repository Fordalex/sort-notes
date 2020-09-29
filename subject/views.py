from django.shortcuts import render, redirect, get_object_or_404
from .models import Subject, Section, Attribute, DropDown, Item
from .forms import subjectForm, sectionForm, attributeForm, dropdownForm, itemForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def subject(request, pk):

    subject = Subject.objects.get(pk=pk)

    context = {
        'subject': subject
    }

    return render(request, 'subject/subject.html', context)

# Add data views

@login_required
def add_subject(request):

    if request.method == "POST":
        form = subjectForm(request.POST, request.FILES)
        if form.is_valid:
            subject = form.save(commit=False)
            subject.user = request.user
            subject.save()
            return redirect('menu')

    context = {
        'subjectForm': subjectForm
    }

    return render(request, 'subject/add_subject.html', context)

@login_required
def add_section(request, pk):
    """
    Display section form and add data.
    """

    subject = Subject.objects.get(pk=pk)

    if request.method == "POST":
        Section.add_subject_section(request, sectionForm, subject)
        return redirect('subject', pk)

    context = {
        'sectionForm': sectionForm,
        'subject': subject,
    }

    return render(request, 'subject/add_section.html', context)

@login_required
def add_attribute(request, pk, subject_pk):

    section = Section.objects.get(pk=pk)

    if request.method == "POST":
        form = attributeForm(request.POST)
        if form.is_valid:
            attribute = form.save(commit=False)
            attribute.save()
            section.attribute.add(attribute.id)
            
            return redirect('subject', subject_pk)

    context = {
        'attributeForm': attributeForm
    }

    return render(request, 'subject/add_attribute.html', context)

@login_required
def add_dropdown(request, attribute_pk, subject_pk):

    attribute = Attribute.objects.get(pk=attribute_pk)

    if request.method == "POST":
        form = dropdownForm(request.POST)
        if form.is_valid:
            dropdown = form.save(commit=False)
            dropdown.save()
            attribute.dropdown.add(dropdown.id)
            
            return redirect('subject', subject_pk)

    context = {
        'dropdownForm': dropdownForm
    }

    return render(request, 'subject/add_dropdown.html', context)

@login_required
def add_item(request, pk, subject_pk):

    dropdown = DropDown.objects.get(pk=pk)

    if request.method == "POST":
        form = itemForm(request.POST)
        if form.is_valid:
            item = form.save(commit=False)
            item.save()
            dropdown.item.add(item.id)
            
            return redirect('subject', subject_pk)

    context = {
        'itemForm': itemForm
    }

    return render(request, 'subject/add_item.html', context)

# Edit data views

@login_required
def edit_subject(request, subject_pk):

    subject = get_object_or_404(Subject, pk=subject_pk)

    if request.method == "POST":
        title = request.POST.get('title')
        information = request.POST.get('information')
        
        subject.title = title
        subject.information = information
    
        if request.POST.get('change_image'):
            image = request.FILES.get('image')
            subject.image = image

        subject.save()

        return redirect('menu')

    context = {
        'subject': subject
    }

    return render(request, 'subject/edit_subject.html', context)

@login_required
def edit_section(request, section_pk, subject_pk):

    section = get_object_or_404(Section, pk=section_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)

    if request.method == "POST":
        section.title = request.POST.get('title')
        section.save()

        return redirect('subject', subject_pk)

    context = {
        'section': section,
        'subject': subject,
    }

    return render(request, 'subject/edit_section.html', context)

@login_required
def edit_attribute(request, attribute_pk, subject_pk):

    attribute = get_object_or_404(Attribute, pk=attribute_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)

    if request.method == "POST":
        attribute.title = request.POST.get('title')
        attribute.save()

        return redirect('subject', subject_pk)

    context = {
        'attribute': attribute,
        'subject': subject,
    }

    return render(request, 'subject/edit_attribute.html', context)

@login_required
def edit_dropdown(request, dropdown_pk, subject_pk):

    dropdown = get_object_or_404(DropDown, pk=dropdown_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)

    if request.method == "POST":
        title = request.POST.get('title')
        icon = request.POST.get('icon')
        
        dropdown.title = title
        dropdown.icon = icon

        dropdown.save()

        return redirect('subject', subject_pk)

    context = {
        'dropdown': dropdown,
        'subject': subject,
    }

    return render(request, 'subject/edit_dropdown.html', context)

    
@login_required
def edit_item(request, item_pk, subject_pk):

    item = get_object_or_404(Item, pk=item_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)

    if request.method == "POST":
        item.title = request.POST.get('title')
        item.website = request.POST.get('website')
        item.save()

        return redirect('subject', subject_pk)

    context = {
        'item': item,
        'subject': subject,
    }

    return render(request, 'subject/edit_item.html', context)

# Remove data

def remove_data(request, data_type ,pk, subject_pk):

    if data_type == 'subject':
        subject = get_object_or_404(Subject, pk=pk)
        subject.delete()
    elif data_type == 'dropdown':
        dropdown = get_object_or_404(DropDown, pk=pk)
        dropdown.delete()
        return redirect('subject', subject_pk)
    elif data_type == 'section':
        section = get_object_or_404(Section, pk=pk)
        section.delete()
        return redirect('subject', subject_pk)
    elif data_type == 'attribute':
        attribute = get_object_or_404(Attribute, pk=pk)
        attribute.delete()
        return redirect('subject', subject_pk)
    elif data_type == 'item':
        item = get_object_or_404(Item, pk=pk)
        item.delete()
        return redirect('subject', subject_pk)

    return redirect('menu')
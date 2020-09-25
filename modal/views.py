from django.shortcuts import render, get_object_or_404
from subject.models import Subject, Item
from .models import Modal

# Create your views here.
def modal(request, subject_pk, item_pk):

    item = get_object_or_404(Item, pk=item_pk)
    subject = get_object_or_404(Subject, pk=subject_pk)
    print(item.modal.all())

    context = {
        'item': item,
        'subject': subject,
    }

    return render(request, 'modal/home.html', context)
from django.shortcuts import render
from subject.models import Subject

# Create your views here.
def home(request):
    subjects = Subject.objects.all()

    context = {
        'subjects': subjects,
    }

    return render(request, 'menu/home.html', context)
from django.shortcuts import render
from subject.models import Subject
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    subjects = Subject.objects.all()

    context = {
        'subjects': subjects,
    }

    return render(request, 'menu/home.html', context)
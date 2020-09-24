from django.shortcuts import render, get_object_or_404
from subject.models import Subject
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    subjects = Subject.objects.filter(user=request.user)

    context = {
        'subjects': subjects,
    }

    return render(request, 'menu/home.html', context)
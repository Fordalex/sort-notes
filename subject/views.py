from django.shortcuts import render

# Create your views here.
def subject(request):

    return render(request, 'subject/subject.html')
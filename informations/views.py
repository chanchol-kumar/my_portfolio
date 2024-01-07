from django.shortcuts import render,redirect
from informations.forms import FeedbackForm
from informations.models import FeedbackModel


def home(request):
    return render(request,'base.html');

def about(request):
    return render(request,'about.html');

def blog(request):
    return render(request, 'blog.html')

def project(request):
    return render(request, 'project.html')

def contact(request):
    return render(request, 'contact.html')

def skill(request):
    return render(request, 'skill.html')


def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback_list.html', {'form': form})


def feedback_list(request):
    data = FeedbackModel.objects.all()
    return render(request, 'feedback_list.html', {'data': data})
from django.shortcuts import render,redirect
from informations.forms import FeedbackForm
from informations.models import FeedbackModel,BlogModel,SkillModel,ProjectModel


def home(request):
    return render(request,'base.html');

def about(request):
    return render(request,'about.html');

def blog(request):
    blog_posts = BlogModel.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def skill(request):
    skill_posts = SkillModel.objects.all()
    return render(request, 'skills.html', {'skill_posts': skill_posts})

def project(request):
    project_posts = ProjectModel.objects.all()
    return render(request, 'project.html', {'project_posts': project_posts})

def contact(request):
    return render(request, 'contact.html')


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
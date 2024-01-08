from django.shortcuts import render,redirect
from informations.forms import FeedbackForm, UserContactForm
from informations.models import FeedbackModel, BlogModel, SkillModel, ProjectModel, UserContactModel

def about(request):
    return render(request,'about.html');

def contact(request):
    return render(request,'contact.html');

def blog(request):
    blog_posts = BlogModel.objects.all()
    return render(request, 'blog.html', {'blog_posts': blog_posts})

def skill(request):
    skill_posts = SkillModel.objects.all()
    return render(request, 'skills.html', {'skill_posts': skill_posts})

def project(request):
    project_posts = ProjectModel.objects.all()
    return render(request, 'project.html', {'project_posts': project_posts})


############################################################
def contact_form(request):
    if request.method == 'POST':
        form1 = UserContactForm(request.POST)
        if form1.is_valid():
            form1.save()
            return redirect('show_user_comment')
    else:
        form1 = UserContactForm()
    return render(request, 'about.html', {'form1': form1})

def show_user_comment(request):
    data = UserContactModel.objects.all()
    return render(request, 'about.html',{'data':data})
############################################################


###########################################################
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_feedback')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def show_feedback(request):
    data = FeedbackModel.objects.all()
    return render(request, 'feedback.html',{'data':data})
###########################################################

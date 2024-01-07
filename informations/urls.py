from django.urls import path
from informations.views import home,about,feedback ,feedback_list,blog,project,contact,skill

urlpatterns = [
    path('',home,name = 'homepage'),
    path('about/',about,name = 'about'),
    path('feedback/',feedback,name = 'feedback'),
    path('blog/',blog,name = 'blog'),
    path('contact/',contact,name = 'contact'),
    path('project/',project,name = 'project'),
    path('skill/',skill,name = 'skill'),
    path('feedback_list/',feedback_list,name = 'feedback_list'),
]

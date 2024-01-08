from django.urls import path
from informations.views import about,feedback,blog,project,skill,feedback,contact

urlpatterns = [
    path('',about,name = 'about'),
    path('feedback/',feedback,name = 'feedback'),
    path('blog/',blog,name = 'blog'),
    path('contact/',contact,name = 'contact'),
    path('project/',project,name = 'project'),
    path('skill/',skill,name = 'skill'),
    path('feedback/',feedback,name = 'feedback'),
]

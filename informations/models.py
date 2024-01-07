from django.db import models
from informations.constant import CHOICE_LIST


class FeedbackModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    # image = models.FileField(upload_to='templates/feed_img/')
    feedback = models.TextField()
    rating = models.CharField(max_length=30, choices=CHOICE_LIST)
    def __str__(self):
        return self.name
    

class BlogModel(models.Model):
    # image = models.FileField(upload_to='templates/blog_img/')
    title = models.CharField(max_length = 100)
    descriptions = models.TextField(max_length = 1000)
    def __str__(self):
        return self.title
    
    
class ProjectModel(models.Model):
    title = models.CharField(max_length = 100)
    descriptions = models.TextField(max_length = 1000)
    def __str__(self):
        return self.title
    

class UploadCV(models.Model):
    upload = models.FileField(upload_to='templates/cv_pdfs/')
    def __str__(self):
        return str(self.upload)
    

class ContactModel(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    query = models.TextField(max_length = 100)
    def __str__(self):
        return self.name
    

    
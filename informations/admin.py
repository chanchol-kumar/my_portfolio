from django.contrib import admin
from informations.models import FeedbackModel,BlogModel,ProjectModel,UploadCV,ContactModel

class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','feedback','rating')
    
admin.site.register(FeedbackModel, FeedbackModelAdmin)

admin.site.register(BlogModel)    
admin.site.register(ProjectModel)    
admin.site.register(UploadCV)    
admin.site.register(ContactModel)    

from django.contrib import admin
from informations.models import FeedbackModel,BlogModel,ProjectModel,UserContactModel,UploadCV,SkillModel

class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('name','email','feedback','rating')
    
admin.site.register(FeedbackModel, FeedbackModelAdmin)

admin.site.register(BlogModel)    
admin.site.register(SkillModel)    
admin.site.register(ProjectModel)    
admin.site.register(UploadCV)    


# class UserContactModelAdmin(admin.ModelAdmin):
#     list_display = ('name','email','subject')
    
# admin.site.register(UserContactModel, UserContactModelAdmin)


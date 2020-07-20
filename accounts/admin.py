from django.contrib import admin
from .models import  UserProfile,Language,lottery
# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address', 'phone','city','country','language','currency','image_tag']
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Language)
admin.site.register(lottery)
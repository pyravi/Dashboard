from django.db import models
from currencies.models import Currency
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# Create your models here.


class lottery(models.Model):
    lottery = models.TextField() 
    
    def __str__(self):
        return self.lottery
        
class Language(models.Model):
    name= models.CharField(max_length=20)
    code= models.CharField(max_length=5)
    status=models.BooleanField()
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
        
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)
    image = models.ImageField(blank=True, upload_to='images/users/')
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True,blank=True)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, null=True,blank=True)


    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' ' + self.user.last_name + ' [' + self.user.username + '] '

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
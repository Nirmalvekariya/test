from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.PROTECT)
    #first_name=models.CharField(max_length=30,default='')
    #last_name=models.CharField(max_length=20,default='')
    #email=models.EmailField(default='')
    oid=models.CharField(max_length=20,default='')
    rio=models.CharField(max_length=20,default='')
    #password1 = models.CharField(max_length=15, default='')
    #password2 = models.CharField(max_length=15, default='')

    def __str__(self):
        return self.user.first_name
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)



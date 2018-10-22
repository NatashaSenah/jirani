from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
  if created:
      Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
  instance.profile.save()
class Neighbourhood(models.Model):
    neighbourhood_image = models.ImageField(upload_to = 'image/',null = True)
    neighbourhood_name = models.TextField()
    neighbourhood_location = models.TextField()
    neighbourhood_occupant = models.TextField()

    def __str__(self):
        return self.neighbourhood_name
    def create_neighbourhood(self):
        self.create()
    def delete_neighbourhood(self):
        self.delete()
    @classmethod
    def search_by_title(cls,search_term):
        neighbourhood = cls.objects.filter(title__icontains=search_term)
        return neighbourhood
class Profile(models.Model):
    profile_image = models.ImageField(upload_to = 'image/',null = True)
    user = models.OneToOneField(User)
    neighbourhood = models.ForeignKey(Neighbourhood,null =True)
    email = models.EmailField() 
    phone_number = models.CharField(max_length = 10,blank =False)
class Business(models.Model):
    business_image = models.ImageField(upload_to = 'image/',null = True)
    business_name = models.TextField()
    user = models.ForeignKey(User)
    neighbourhood = models.ForeignKey(Neighbourhood)
    email = models.EmailField() 
    def __str__(self):
        return self.business_name
    def create_business(self):
        self.create()
    def delete_business(self):
        self.delete() 
    
    
    

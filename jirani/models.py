from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
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
class User(models.Model):
    user_name = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood)
    email = models.EmailField()  
    phone_number = models.CharField(max_length = 10,blank =False)
class Business(models.Model):
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
    
    
    

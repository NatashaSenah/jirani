from django.db import models

# Create your models here.
class Neighbourhood(models.Model):
    neighbourhood_name = models.TextField()
    neighbourhood_location = models.TextField()
    neighbourhood_occupant = models.TextField()
    def __str__(self):
        return self.image_name
    def create_neighbourhood(self):
        self.create()
    def delete_neighbourhood(self):
        self.delete()
class User(models.model):
    user_name = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood)
    email = models.EmailField()  
    phone_number = models.CharField(max_length = 10,blank =False)
    

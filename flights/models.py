from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=64, unique=True)
    city = models.CharField(max_length=64)
    destiniation = models.ManyToManyField

    def __str__(self):
        return f' {self.city} {self.code}'
    

class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete =models.CASCADE, related_name= 'departure')
    destination = models.ForeignKey(Airport, on_delete =models.CASCADE, related_name= 'arrival')
    duration = models.IntegerField()


    def __str__(self):
        return f"{self.id}: {self.origin} to {self.destination}"

class Passenger(models.Model):
  fname=models.CharField(max_length=64, unique=True)
  lname =models.CharField(max_length=64, unique=True)
  flights = models.ManyToManyField(Flight,blank=True,related_name='passengers')
  
  
  def __str__(self):
        return f"{self.fname} {self.lname}"
  

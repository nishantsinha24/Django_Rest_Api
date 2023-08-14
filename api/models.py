from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT' , 'IT'), ('NON IT' , 'NON IT'), ('MOBILE PHONES','MOBILE PHONES')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def __str__(self) :
        return self.name  +', ' +self.location
    
#Creating Employee models here 

class Employee (models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    phone = models.IntegerField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50 , choices=(('Manager' , 'Manager'), ('Software Engineer' , 'Software Engieer'), ('Software Tester','Software Tester')))
    
    
    Company = models.ForeignKey(Company ,on_delete=models.CASCADE)
    
    
    
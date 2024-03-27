from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=100,null=True)
    age=models.CharField(max_length=100,null=True)
    city=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return f"{self.name},{self.mobile}"
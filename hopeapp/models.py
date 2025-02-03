from django.db import models
from django.utils import timezone
# Create your models here.
class Announcements(models.Model):
    title = models.CharField(max_length=250)
    message = models.CharField(max_length=250)
    
    def __str__(self):
        return self.title
    
class Events(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title

class Newsletter(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title
    
class Programmes(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title

class Team(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title
    
class Gallery(models.Model):
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return str(self.image)
    
class Connect(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Mission(models.Model):
    descriprion = models.TextField()
    
    def __str__(self):
        return self.descriprion
    
class Vission(models.Model):
    descriprion = models.TextField()
    
    def __str__(self):
        return self.descriprion
    
class About(models.Model):
    description = models.TextField()
    
    def __str__(self):
        return self.description
    
class Donation(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    mpesa_code = models.CharField(max_length=50, blank=True, default="")
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.amount}"

class Volunteer(models.Model):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField()
    reason = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=255,null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True,blank=True)
    email = models.EmailField()
    message = models.TextField()
    # created_at = models.DateTimeField(default=timezone)

    def __str__(self):
        return self.name


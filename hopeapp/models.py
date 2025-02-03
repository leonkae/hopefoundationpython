from django.db import models

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
    
class Donation(models.Model):
    name = models.CharField(max_length=250)
    mpesa_number = models.CharField(max_length=100)
    donated_ammount = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.name

class Volunteer(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.EmailField()
    
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
    

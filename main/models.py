from django.db import models
# Create your models here.


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , null=True)

class Projects(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='logos/')
    description = models.TextField()
    website = models.URLField(max_length=250)

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery/')
    name = models.CharField(max_length=100)
    description = models.TextField()

from ckeditor.fields import RichTextField
from django.db import models

# Our Services Section
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Service Title")
    short_description = RichTextField(verbose_name="Short Description")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Service Image")

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name="Project Title")
    short_description = RichTextField(verbose_name="Short Description")
    image = models.ImageField(upload_to='projects/', blank=True, null=True, verbose_name="Project Image")

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title = models.CharField(max_length=200, verbose_name="Title")
    description = RichTextField(verbose_name="Description")
    image = models.ImageField(upload_to='about_us/', blank=True, null=True, verbose_name="Image")
    
    def __str__(self):
        return self.title

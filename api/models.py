from django.db import models

# Our Services Section
class Service(models.Model):
    title = models.CharField(max_length=100, verbose_name="Service Title")
    short_description = models.TextField(verbose_name="Short Description")
    image = models.ImageField(upload_to='services/', blank=True, null=True, verbose_name="Service Image")

    def __str__(self):
        return self.title

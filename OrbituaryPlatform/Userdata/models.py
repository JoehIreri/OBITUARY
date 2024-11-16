from django.db import models

# Create your models here.
class Userdata(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=False)
    middle_name = models.CharField(max_length=50,null=True, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=False)
    date_of_birth = models.DateField(blank=False, null=True)
    date_of_death = models.DateField(blank=False, null=True)
    uology = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_image/', blank=True, null=True)
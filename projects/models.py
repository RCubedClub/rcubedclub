from django.db import models
from django.utils.text import slugify

# Create your models here.
class project(models.Model):
    team_name = models.CharField(max_length=100)
    project_title = models.CharField(max_length=150)
    project_description = models.TextField()
    source_code = models.URLField()
    webpage = models.URLField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    developing_or_developed = models.BooleanField(default=0)
    key = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return str(self.project_title)

class information(models.Model):
    info_title = models.CharField(max_length=150)
    info = models.TextField()
    image = models.ImageField(null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.info_title)

class teams(models.Model):
    Team_Name = models.CharField(max_length=100)
    Name = models.CharField(max_length=50)
    Facebook_Profile_Link = models.URLField()
    Github_Profile_Link = models.URLField()
    Linkedin_Profile_Link = models.URLField(null=True, blank=True)
    Image = models.ImageField(width_field="width_field", height_field="height_field")
    Key = models.CharField(max_length=100)
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    active = models.BooleanField(default=1)

    def __str__(self):
        return str(self.Name)

class list_of_keys(models.Model):
    key = models.CharField(max_length=50)

    def __str__(self):
        return str(self.key)
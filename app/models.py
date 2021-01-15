from django.db import models

# Create your models here.
class Logo(models.Model):
    main_logo=models.ImageField(upload_to="logo")
    notification=models.ImageField(upload_to="notification")
class VideoData(models.Model):
    title=models.CharField(max_length=100,blank=False)
    video=models.FileField(upload_to="video/%y")
    thimnail =models.ImageField(upload_to='Thumnail',blank=True)
    video_length=models.IntegerField(blank=True)
    def __str__(self):
        return self.title

class Trending(models.Model):
    title=models.CharField(max_length=100,blank=False)
    video=models.FileField(upload_to="video/%y")
    thimnail =models.ImageField(upload_to='Thumnail',blank=True)
    video_length=models.IntegerField(blank=True)
    def __str__(self):
        return self.title

class Recently(models.Model):
    title=models.CharField(max_length=100,blank=False)
    video=models.FileField(upload_to="video/%y")
    thimnail =models.ImageField(upload_to='Thumnail',blank=True)
    video_length=models.IntegerField(blank=True)
    def __str__(self):
        return self.title

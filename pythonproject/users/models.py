from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    gender_choices={
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other')
    }
    image = models.ImageField(upload_to='profile_pics', default='profile_pics/default.jpg', verbose_name='Profile Picture')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(default='', max_length=100)
    gender = models.CharField(max_length=10, choices=gender_choices, default='', null='true', blank='true')
    
    
    def __str__(self):
        return f"{ self.user.username }'s Profile"
    
    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path).convert('RGB')
        if img.height > 130 or img.width > 130:
            output_size = (130, 130)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Subscriber(models.Model):
    name=models.CharField(max_length=30,default='')
    email=models.EmailField(default='', null='False')
    to_name=models.ForeignKey(Profile,default=None,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
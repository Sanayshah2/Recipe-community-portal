from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone

# Create your models here.
class Food(models.Model):
    category_choices=(
        ('Non veg','Non veg'),
        ('Veg','Veg'),
        ('North Indian','North Indian'),
        ('Chinese','Chinese'),
        ('Italian','Italian'),
        ('Spanish','Spanish'),
        ('American','American'),
    )
    difficulty_choices=(
        ('Easy','Easy'),
        ('Medium','Medium'),
        ('Hard','Hard'),
       
    )

  
    
    author=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    name=models.CharField(max_length=30,default='')
    desc=models.CharField(max_length=30,default='') 
    category=models.CharField(max_length=30,default='',choices=category_choices)
    servings=models.CharField(max_length=30,default='')
    prep_time=models.CharField(max_length=30,default='')
    ingredients=models.TextField(default='')    
    cook_time=models.CharField(max_length=30,default='')
    difficulty=models.CharField(max_length=30,default='',choices=difficulty_choices)
    steps_to_follow=models.TextField(default='')
    image=models.ImageField(upload_to='food',default="")
    date_posted =models.DateTimeField(default=timezone.now)
    visits=models.IntegerField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=30,default='')    
    image=models.ImageField(upload_to='category',default="")

    def __str__(self):
        return self.name


class Comment(models.Model):
    food=models.ForeignKey(Food,on_delete=models.CASCADE,default='')
    author=models.CharField(max_length=30, default='Anonymous', null='False')
    comment=models.TextField(null='False')
    rating = models.IntegerField(blank='true', validators=[MaxValueValidator(5), MinValueValidator(1)], default=1,)
    date_posted =models.DateTimeField(default=timezone.now)
    
    
    def __str__(self):
        return f"{self.food.author.username}'s {self.food.name}'s {self.author}'s comment"
    
    
    class Meta:
        ordering=['-date_posted']


    

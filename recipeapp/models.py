from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recipes/')
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='recipes')
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

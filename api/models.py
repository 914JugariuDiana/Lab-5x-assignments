
# Create your models here.
from django.db import models

class Chef(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    prizes = models.IntegerField()
    dob = models.DateField(auto_now_add=True)
    cnp = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.firstName + self.lastName

class Ingredient(models.Model):
    ingredientName = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    runningLow = models.BooleanField()
    expirationDate = models.DateField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.ingredientName

class Food(models.Model):
    foodName = models.CharField(max_length=100)
    proteinGrams = models.IntegerField()
    sugarGrams = models.IntegerField()
    expirationDate = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    chefCreator = models.ForeignKey(Chef, related_name='foods', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.foodName

    
class ReceipeIndications(models.Model):
    foodId = models.ForeignKey(Food, related_name = 'food', on_delete=models.CASCADE)
    ingredientId = models.ForeignKey(Ingredient, related_name = 'ingredient', on_delete=models.CASCADE)
    quantityOfIngredient = models.IntegerField()
    specifications = models.CharField(max_length=1000)

    



from rest_framework import serializers
from .models import Food, Chef, Ingredient, ReceipeIndications

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'foodName', 'proteinGrams', 'sugarGrams', 'expirationDate', 'quantity', 'chefCreator']

class ChefSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chef
        fields = ('__all__')

class ReceipeIndicationsForOneIngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceipeIndications
        fields = ['quantityOfIngredient', 'specifications']

class IngredientSerializer(serializers.ModelSerializer):
    
    #foodId = FoodSerializer(many = True, read_only=True)
    #quantityOfIngredient = ReceipeIndicationsForOneIngredientSerializer(source='recipeindications', many = True, read_only = True)
    class Meta:
        model = Ingredient
        fields = ['id', 'ingredientName', 'location', 'runningLow', 'expirationDate', 'quantity']

# class IngredientAverageQuantitySerializer (serializers.ModelSerializer):
#     foodId = FoodNameSerializer(read_only=True)
#     ingredientId = IngredientNameSerializer(read_only=True)
#     class Meta:
#         model = ReceipeIndications
#         fields = ['foodId', 'ingredientId', 'quantityOfIngredient']

class FoodSerializerDetail(serializers.ModelSerializer):
    chef = ChefSerializer(source='chefCreator', read_only = True)

    class Meta:
        model = Food
        fields = ['id', 'foodName', 'proteinGrams', 'sugarGrams', 'expirationDate', 'quantity', 'chefCreator', 'chef']

class ChefSerializerDetail(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Chef
        fields = ['id', 'firstName', 'lastName', 'prizes', 'dob', 'cnp', 'foods']

class ReceipeIndicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceipeIndications
        fields =['id', 'foodId', 'ingredientId', 'quantityOfIngredient', 'specifications']


class FoodNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['foodName']

class IngredientNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['ingredientName']

class ChefFoodSerializer(serializers.ModelSerializer):
    avgQuantity = serializers.FloatField()

    class Meta:
        model = Chef
        fields = ['id', 'firstName', 'lastName', 'prizes', 'dob', 'cnp', 'avgQuantity']

class FoodIngredientSerializer(serializers.ModelSerializer):
    avgQuantityOfIngredients = serializers.FloatField()

    class Meta:
        model = Food
        fields = ['id', 'foodName', 'proteinGrams', 'sugarGrams', 'expirationDate', 'quantity', 'chefCreator', 'avgQuantityOfIngredients']



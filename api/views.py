from rest_framework import generics
from .models import Food, Chef, Ingredient, ReceipeIndications
from .serializers import FoodSerializer, ChefSerializer, IngredientSerializer, ChefSerializerDetail, \
    FoodSerializerDetail, ReceipeIndicationsSerializer, ChefFoodSerializer,\
    FoodIngredientSerializer
from django.db.models import Avg

class FoodList(generics.ListCreateAPIView):
    serializer_class = FoodSerializer
    queryset = Food.objects.all()
    
class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = FoodSerializerDetail
    queryset = Food.objects.all()

class ChefList(generics.ListCreateAPIView):
    serializer_class = ChefSerializer
    queryset = Chef.objects.all()        
    
class ChefDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ChefSerializerDetail
    queryset = Chef.objects.all()
    
class IngredientList(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()        
    
class IngredientDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

class ReceipeIndicationsList(generics.ListCreateAPIView):
    serializer_class = ReceipeIndicationsSerializer
    queryset = ReceipeIndications.objects.all()

class ReceipeIndicationsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReceipeIndicationsSerializer
    queryset = ReceipeIndications.objects.all()

class IngredientQuantity(generics.ListCreateAPIView):
    serializer_class = IngredientSerializer

    def get_queryset(self):
        queryset = Ingredient.objects.all()
        var = self.request.GET.get('quantity', 0)
        if var is not None:
            queryset = queryset.filter(quantity__gt=var)
        return queryset
        
class OrderChefs(generics.ListCreateAPIView):
    serializer_class = ChefFoodSerializer
    def get_queryset(self):
        queryset = Chef.objects.annotate(avgQuantity=Avg('foods__quantity')).order_by('avgQuantity')
        return queryset
    

class OrderFood(generics.ListCreateAPIView):
    serializer_class = FoodIngredientSerializer
    def get_queryset(self):
        queryset = Food.objects\
            .annotate(avgQuantityOfIngredients=Avg('food__ingredientId__quantity'))\
            .order_by('avgQuantityOfIngredients')
        return queryset
    
        
            
    


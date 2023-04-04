'

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    path('food/', views.FoodList.as_view()),
    path('food/<int:pk>/', views.FoodDetail.as_view()),
    path('chef/', views.ChefList.as_view()),
    path('chef/<int:pk>/', views.ChefDetail.as_view()),
    path('ingredients/', views.IngredientList.as_view()),
    path('ingredients/<int:pk>/', views.IngredientDetail.as_view()),
    path('recipe/', views.ReceipeIndicationsList.as_view()),
    path('recipe/<int:pk>/', views.ReceipeIndicationsDetail.as_view()), 
    path('filterIngredients/', views.IngredientQuantity.as_view()),
    path('orderChefs/', views.OrderChefs.as_view()),
    path('orderFoods/', views.OrderFood.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
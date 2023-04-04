from django.contrib import admin
from .models import Food, Chef, Ingredient

admin.site.register(Chef)
admin.site.register(Ingredient)
admin.site.register(Food)
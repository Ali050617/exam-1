from django.shortcuts import render
from .models import Meals

def meals_list(requests):
    meal_name = requests.GET.get('meal_name')
    ingredients = requests.GET.get('ingredients')
    price = requests.GET.get('price')
    type = requests.GET.get('type')
    cuisine = requests.GET.get('cuisine')
    if (meal_name and ingredients and price and type and cuisine):
        Meals.objects.create(
            meal_name=meal_name,
            ingredients=ingredients,
            price=price,
            type=type,
            cuisine=cuisine
        )
    meal = Meals.objects.all()
    ctx ={'meals': meal}
    return render(requests, 'meals/meals-list.html', ctx)


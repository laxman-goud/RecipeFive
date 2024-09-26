from django.shortcuts import render, HttpResponse 
from django.shortcuts import render, get_object_or_404, redirect

from .recipes_list import recipes  # Import the recipes list

# Home view
def home(request):
    return render(request, 'index.html')

# Recipe detail view
def recipe_detail(request, recipe_id):
    # Find the recipe with the given ID in the list
    recipe = next((recipe for recipe in recipes if recipe['id'] == recipe_id), None)

    if not recipe:
        # Handle recipe not found (Optional: Render a 404 page)
        return render(request, '404.html')

    # Pass the recipe data to the template
    return render(request, 'recipe.html', {'recipe': recipe})

# Login view
def login_view(request):
    return render(request, 'login_page.html')

# Registration view
def registration_view(request):
    return render(request, 'registration.html')


def cart_view(request, recipe_id):
    # Get the specific recipe by ID
    recipe = next((item for item in recipes if item['id'] == recipe_id), None)
    
    # Check if the recipe exists; if not, return a 404 error
    if recipe is None:
        return render(request, '404.html', status=404)  # Optional: customize your 404 page

    # Pass the specific recipe as a list to the template for iteration
    return render(request, 'cart.html', {'recipes': [recipe]})

def buynow(request, recipe_id):
    # Find the recipe based on the provided recipe_id
    recipe = next((item for item in recipes if item['id'] == recipe_id), None)

    if recipe is None:
        # Handle the case where the recipe is not found
        return render(request, '404.html')  # Or any other error page

    return render(request, 'buynow.html', {'recipe': recipe})
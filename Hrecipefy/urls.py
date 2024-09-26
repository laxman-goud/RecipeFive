from django.contrib import admin
from django.urls import path
from Hrecipefy import views

urlpatterns = [
    path("", views.home, name='home'),                      # Home page
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),  # Recipe detail page
    path('login/', views.login_view, name='login'),         # Login page
    path('register/', views.registration_view, name='register'),  # Registration page
    path('cart/<int:recipe_id>/', views.cart_view, name='cart'),
    path('buynow/<int:recipe_id>/', views.buynow, name='buynow'),
]

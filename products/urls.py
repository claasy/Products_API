from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_lists),
    path('<int:pk>/', views.product_detail),
]
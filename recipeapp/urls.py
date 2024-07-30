from django.urls import path
from .views import recipe_list, recipe_detail, recipe_new, recipe_edit, recipe_delete,recipe_list, signup

urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('signup/', signup, name='signup'),
    path('recipe/<int:pk>/', recipe_detail, name='recipe_detail'),
    path('recipe/new/', recipe_new, name='recipe_new'),
    path('recipe/<int:pk>/edit/', recipe_edit, name='recipe_edit'),
    path('recipe/<int:pk>/delete/', recipe_delete, name='recipe_delete'),
    path('category/<int:category_id>/',recipe_list, name='recipe_by_category'),
]

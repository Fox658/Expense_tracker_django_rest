from .views import (
    UsersView,
    ExpensesView,
    CategoriesView
)
from django.urls import path

urlpatterns = [
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:user_id>', UsersView.as_view(), name='user-edit'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('categories/<uuid:category_id>', CategoriesView.as_view(), name='categories-edit'),
]

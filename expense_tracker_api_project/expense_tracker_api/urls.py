from .views import (
    HelloWorldView,
    UsersView,
    ExpensesView,
    BudgetsView,
    CategoriesView
)
from django.urls import path

urlpatterns = [
    path('hello-world/', HelloWorldView.as_view(), name='hello-world'),
    path('users/', UsersView.as_view(), name='users'),
    path('users/<int:user_id>', UsersView.as_view(), name='user-edit'),
]

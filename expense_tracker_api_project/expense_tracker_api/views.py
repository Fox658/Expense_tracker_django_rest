from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer, ExpenseSerializer
from .models import Category, Expense

import os

# Create your views here.
# curl -X PUT -H "Content-Type: application/json" -d '{"data":{"username": "testuser", "id": 1}}' http://127.0.0.1:8000/expense-tracker-api/users/1

class UsersView(APIView):

    def get(self, request, format=None):
        return Response({"data": [{"id": "1", "name": "Juan", "age": 34}]})

    def post(self, request):
        print("User POST DATA: ", request.data)
        return Response({"status": "OK", "data": request.data})

    def put(self, request, user_id):
        print("user_id:", user_id)
        return Response({"status": "UPDATED", "data": request.data})

    def delete(self, user_id):
        pass

class ExpensesView(APIView):

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass

    def put(self, request, expense_id):
        pass

    def delete(self, expense_id):
        pass

class CategoriesView(APIView):
    def get(self, request, format=None):

        categories = Category.objects.all()

        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)


    def post(self, request, format=None):
        
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, category_id):
        try:
            category = Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        

    def delete(self, request, category_id):

        try:
            category = Category.objects.get(category_id=category_id)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        category.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



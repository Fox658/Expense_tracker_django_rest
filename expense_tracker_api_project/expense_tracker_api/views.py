from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# curl -X PUT -H "Content-Type: application/json" -d '{"data":{"username": "testuser", "id": 1}}' http://127.0.0.1:8000/expense-tracker-api/users/1
class HelloWorldView(APIView):

    def get(self, request, format=None):
        """
        Hello world endpoint for Django REST Framework (DRF)
        """
        return Response({"data": [{"message": "hello world!"}]})

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

class BudgetsView(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass

    def put(self, request, budget_id):
        pass

    def delete(self, budget_id):
        pass

class CategoriesView(APIView):
    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass

    def put(self, request, category_id):
        pass

    def delete(self, category_id):
        pass

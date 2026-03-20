from .views import HelloWorldView
from django.urls import path

urlpatterns = [
    path('hello-world/', HelloWorldView.as_view(), name='hello-world')
]
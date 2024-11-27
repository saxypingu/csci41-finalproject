# urls.py in your app directory
from django.urls import path
from .views import TestView

urlpatterns = [
    path('test/', TestView.as_view(), name='test_view'),
]

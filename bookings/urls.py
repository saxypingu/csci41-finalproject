# urls.py in your app directory
from django.urls import path
from .views import TestView, OrganizerCreateView, OrganizerListView, OrganizerDetailView

urlpatterns = [
    path('test/', TestView.as_view(), name='test_view'),
    path('organizers/', OrganizerListView.as_view(), name='organizer_list'),
    path('organizer/create/', OrganizerCreateView.as_view(), name='organizer_create'),
    path('organizer/<int:organizer_id>/', OrganizerDetailView.as_view(), name='organizer_detail')
]

# urls.py in your app directory
from django.urls import path
from .views import OrganizerCreateView, OrganizerListView, OrganizerDetailView
from .views import ActivityCreateView, ActivityListView, ActivityDetailView

urlpatterns = [
    path('organizers/', OrganizerListView.as_view(), name='organizer_list'),
    path('organizer/create/', OrganizerCreateView.as_view(), name='organizer_create'),
    path('organizer/<int:organizer_id>/', OrganizerDetailView.as_view(), name='organizer_detail'),
    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activity/create/', ActivityCreateView.as_view(), name='activity_create'),
    path('activity/<int:activity_id>/', ActivityDetailView.as_view(), name='activity_detail')
]

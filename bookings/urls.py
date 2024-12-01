# urls.py in your app directory
from django.urls import path
from .views import OrganizerCreateView, OrganizerListView, OrganizerDetailView, OrganizerUpdateView, OrganizerDeleteView
from .views import ActivityCreateView, ActivityListView, ActivityDetailView, ActivityUpdateView, ActivityDeleteView, BookingDeleteView, ParticipantBookingsView

urlpatterns = [
    path('organizers/', OrganizerListView.as_view(), name='organizer_list'),
    path('organizer/create/', OrganizerCreateView.as_view(), name='organizer_create'),
    path('organizer/<int:organizer_id>/', OrganizerDetailView.as_view(), name='organizer_detail'),
    path('organizer/edit/<int:organizer_id>', OrganizerUpdateView.as_view(), name='organizer_update'),
    path('organizer/delete/<int:organizer_id>/', OrganizerDeleteView.as_view(), name='organizer_delete'),

    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activity/create/', ActivityCreateView.as_view(), name='activity_create'),
    path('activity/<int:activity_id>/', ActivityDetailView.as_view(), name='activity_detail'),
    path('activity/edit/<int:activity_id>', ActivityUpdateView.as_view(), name='activity_update'),
    path('activity/delete/<int:activity_id>/', ActivityDeleteView.as_view(), name='activity_delete'),

    path('bookings/<int:id_number>/', ParticipantBookingsView.as_view(), name='booking_summary'),
        path('bookings/delete/<int:booking_id>/<int:id_number>/', BookingDeleteView.as_view(), name='booking_delete'),


]

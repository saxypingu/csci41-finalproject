# urls.py in your app directory
from django.urls import path
from .views import OrganizerListView, OrganizerDetailView, OrganizerUpdateView, OrganizerDeleteView, org_create
from .views import ActivityCreateView, ActivityListView, ActivityDetailView, ActivityUpdateView, ActivityDeleteView
from .views import ParticipantCreateView, ParticipantDetailView, ParticipantListView
from .views import BookingCreateView, BookingListView, BookingDetailView

urlpatterns = [
    path('organizers/', OrganizerListView.as_view(), name='organizer_list'),
    path('organizer/create/', org_create, name='organizer_create'),
    path('organizer/<int:organizer_id>/', OrganizerDetailView.as_view(), name='organizer_detail'),
    path('organizer/edit/<int:organizer_id>', OrganizerUpdateView.as_view(), name='organizer_update'),
    path('organizer/delete/<int:organizer_id>/', OrganizerDeleteView.as_view(), name='organizer_delete'),

    path('activities/', ActivityListView.as_view(), name='activity_list'),
    path('activity/create/', ActivityCreateView.as_view(), name='activity_create'),
    path('activity/<int:activity_id>/', ActivityDetailView.as_view(), name='activity_detail'),

    path('participants/', ParticipantListView.as_view(), name='participant_list'),
    path('participant/create/', ParticipantCreateView.as_view(), name='participant_create'),
    path('participant/<int:activity_id>/', ParticipantDetailView.as_view(), name='participant_detail'),
    
    path('activity/edit/<int:activity_id>', ActivityUpdateView.as_view(), name='activity_update'),
    path('activity/delete/<int:activity_id>/', ActivityDeleteView.as_view(), name='activity_delete'),

    path('booking/', BookingListView.as_view(), name='booking_list'),
    path('booking/create/', BookingCreateView.as_view(), name='booking_create'),
    path('booking/<int:activity_id>/', BookingDetailView.as_view(), name='booking_detail')
]
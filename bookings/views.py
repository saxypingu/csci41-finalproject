# views.py
from django.views import View
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Organizer, Activity, Participant
from .forms import OrganizerForm, ActivityForm, ParticipantForm

class OrganizerCreateView(View):    
    def get(self, request, *args, **kwargs):
        form = OrganizerForm()
        return render(request, 'bookings/organizer/organizer_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = OrganizerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('organizer_list')  # Redirect to the list of organizers
        return render(request, 'bookings/organizer/organizer_form.html', {'form': form})

class OrganizerListView(View):
    def get(self, request, *args, **kwargs):
        organizers = Organizer.objects.all()
        return render(request, 'bookings/organizer/organizer_list.html', {'organizers': organizers})

class OrganizerDetailView(View):
    def get(self, request, organizer_id, *args, **kwargs):
        organizer = get_object_or_404(Organizer, pk=organizer_id)
        activities = Activity.objects.filter(organizer_id=organizer_id) 
        return render(request, 'bookings/organizer/organizer_detail.html', {'organizer': organizer, 'activities': activities})

class OrganizerUpdateView(View):
    def get(self, request, organizer_id, *args, **kwargs):
        organizer = get_object_or_404(Organizer, pk=organizer_id)
        form = OrganizerForm(instance=organizer)
        return render(request, 'bookings/organizer/organizer_form.html', {'form': form, 'organizer': organizer})

    def post(self, request, organizer_id, *args, **kwargs):
        organizer = get_object_or_404(Organizer, pk=organizer_id)
        form = OrganizerForm(request.POST, instance=organizer)
        if form.is_valid():
            form.save()
            return redirect('organizer_detail', organizer_id=organizer_id)
        return render(request, 'bookings/organizer/organizer_form.html', {'form': form, 'organizer': organizer})

class OrganizerDeleteView(View):
    def post(self, request, organizer_id, *args, **kwargs):
        organizer = get_object_or_404(Organizer, pk=organizer_id)
        organizer.delete()
        return redirect('organizer_list')

class ActivityCreateView(View):    
    def get(self, request, *args, **kwargs):
        form = ActivityForm()
        return render(request, 'bookings/activity/activity_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('activity_list')  # Redirect to the list of activities
        return render(request, 'bookings/activity/activity_form.html', {'form': form})

class ActivityListView(View):
    def get(self, request, *args, **kwargs):
        activities = Activity.objects.all()
        return render(request, 'bookings/activity/activity_list.html', {'activities': activities})

class ActivityDetailView(View):
    def get(self, request, activity_id, *args, **kwargs):
        activity = get_object_or_404(Activity, pk=activity_id)
        return render(request, 'bookings/activity/activity_detail.html', {'activity': activity})
    
class ParticipantCreateView(View):    
    def get(self, request, *args, **kwargs):
        form = ParticipantForm()
        return render(request, 'bookings/participant/participant_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')  # Redirect to the list of participants
        return render(request, 'bookings/participant/participant_form.html', {'form': form})

class ParticipantListView(View):
    def get(self, request, *args, **kwargs):
        participants = Participant.objects.all()
        return render(request, 'bookings/participant/participant_list.html', {'participants': participants})

class ParticipantDetailView(View):
    def get(self, request, activity_id, *args, **kwargs):
        participant = get_object_or_404(Participant, pk=activity_id)
        return render(request, 'bookings/participant/participant_detail.html', {'participant': participant})
    

class ActivityUpdateView(View):
    def get(self, request, activity_id, *args, **kwargs):
        activity = get_object_or_404(Activity, pk=activity_id)
        form = ActivityForm(instance=activity)
        return render(request, 'bookings/activity/activity_form.html', {'form': form, 'activity': activity})

    def post(self, request, activity_id, *args, **kwargs):
        activity = get_object_or_404(Activity, pk=activity_id)
        form = ActivityForm(request.POST, instance=activity)
        if form.is_valid():
            form.save()
            return redirect('activity_detail', activity_id=activity.id)
        return render(request, 'bookings/activity/activity_form.html', {'form': form, 'activity': activity})

class ActivityDeleteView(View):
    def post(self, request, activity_id, *args, **kwargs):
        activity = get_object_or_404(Activity, pk=activity_id)
        activity.delete()
        return redirect('activity_list')

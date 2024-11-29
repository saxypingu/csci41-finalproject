# views.py
from django.views import View
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Organizer, Activity
from .forms import OrganizerForm, ActivityForm

class TestView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("This is a GET response from the TestView!", content_type="text/plain")

    def post(self, request, *args, **kwargs):
        return HttpResponse("POST requests are not yet implemented.", content_type="text/plain", status=400)

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
        return render(request, 'bookings/organizer/organizer_detail.html', {'organizer': organizer})

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
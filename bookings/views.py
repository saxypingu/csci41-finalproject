# views.py
from django.views import View
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Organizer, Activity, Participant, Booking
from .forms import OrganizerForm, ActivityForm
from .models import Organizer, Contact_Person, Activity, Participant
from .forms import OrganizerForm, ContactPersonForm, ActivityForm, ParticipantForm

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
    
def org_create(request):
    if request.method == 'POST':
        orgform = OrganizerForm(request.POST, prefix='organizer')
        conform = ContactPersonForm(request.POST, prefix='contact')
        if orgform.is_valid() and conform.is_valid():
            organizer = Organizer()
            contact_person = Contact_Person()
            organizer.name = orgform.cleaned_data.get('name')
            organizer.organizer_type = orgform.cleaned_data.get('organizer_type')
            organizer.address = orgform.cleaned_data.get('address')
            contact_person.contact_email = conform.cleaned_data.get('contact_email')
            contact_person.contact_name = conform.cleaned_data.get('contact_name')
            contact_person.contact_phone = conform.cleaned_data.get('contact_phone')
            contact_person.save()   
            organizer.contact_person = contact_person
            organizer.save()
            return redirect('organizer_detail', organizer.organizer_id)
    else:
        orgform = OrganizerForm(prefix='organizer')
        conform = ContactPersonForm(prefix='contact')
    return render(request, 'bookings/organizer/organizer_form.html', {'orgform': orgform,
                                                                            'conform': conform})
        
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

class ParticipantCreateView(View):    
    def get(self, request, *args, **kwargs):
        form = ParticipantForm()
        return render(request, 'bookings/participant/participant_form.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')  # Redirect to the list of activities
        return render(request, 'bookings/participant/participant_form.html', {'form': form})

class ParticipantListView(View):
    def get(self, request, *args, **kwargs):
        participants = Participant.objects.all()
        return render(request, 'bookings/participant/participant_list.html', {'participants': participants})

class ParticipantDetailView(View):
    def get(self, request, participant_id, *args, **kwargs):
        participant = get_object_or_404(Participant, pk=participant_id)
        return render(request, 'bookings/participant/participant_detail.html', {'participant': participant})

class ParticipantUpdateView(View):
    def get(self, request, participant_id, *args, **kwargs):
        participant = get_object_or_404(Participant, pk=participant_id)
        form = ParticipantForm(instance=participant)
        return render(request, 'bookings/participant/participant_form.html', {'form': form, 'participant': participant})

    def post(self, request, participant_id, *args, **kwargs):
        participant = get_object_or_404(Participant, pk=participant_id)
        form = ParticipantForm(request.POST, instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_detail', participant_id=participant.id_number)
        return render(request, 'bookings/participant/participant_form.html', {'form': form, 'participant': participant})

class ParticipantDeleteView(View):
    def post(self, request, participant_id, *args, **kwargs):
        participant = get_object_or_404(Participant, pk=participant_id)
        participant.delete()
        return redirect('participant_list')
from django import forms
from .models import Organizer, Organizer_Details, Activity

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'address', 'contact_person_name', 'contact_person_email', 'contact_person_phone', 'organizer_type']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['organizer', 'name', 'location', 'date', 'start_time', 'end_time', 'expected_participants']
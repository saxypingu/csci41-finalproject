from django import forms
from .models import Organizer, Activity, Participant

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'address', 'contact_person_name', 'contact_person_email', 'contact_person_phone', 'organizer_type']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['organizer', 'name', 'location', 'date', 'start_time', 'end_time', 'expected_participants']

# class BookingForm(forms.ModelForm):
#     class Meta:
#         model = Booking 
#         fields = ['participant', 'activity', 'attended']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields =  ['id_number', 'name', 'birth_date','department', 'participant_type']
        widgets = {
            'organizer': forms.Select(attrs={'placeholder': 'Select organizer'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter activity name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter activity location'}),
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'expected_participants': forms.NumberInput(attrs={'placeholder': 'Enter expected participants'}),
        }

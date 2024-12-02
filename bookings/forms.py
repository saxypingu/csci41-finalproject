from django import forms
from .models import Organizer, Activity
from .models import Organizer, Contact_Person, Activity, Participant

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'organizer_type', 'address']
        
class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = Contact_Person
        fields = ['contact_email', 'contact_name', 'contact_phone']

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['id_number', 'name', 'birth_date', 'participant_type', 'year_level','rank', 'role','course_code','assigned_division']
        widgets = {
            'id_number': forms.NumberInput(attrs={'placeholder': 'ID Number'}),
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'birth_date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'participant_type': forms.Select(attrs={'placeholder': 'Student, Staff, or Faculty?'}),
            'year_level': forms.Select(attrs={'placeholder': 'Year Level (For students only)'}),
            'rank': forms.TextInput(attrs={'placeholder': 'Professor Rank (For faculty only)'}),
            'role': forms.TextInput(attrs={'placeholder': 'Role (For staff only)'}),
            'course_code': forms.TextInput(attrs={'placeholder': 'Course code (For students and faculty only)'}),
            'assigned_division': forms.TextInput(attrs={'placeholder': 'Assigned Division (For staff only)'}),
        }

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['organizer', 'name', 'location', 'date', 'start_time','end_time', 'expected_participants']
        widgets = {
            'organizer': forms.Select(attrs={'placeholder': 'Select organizer'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter activity name'}),
            'location': forms.Select(attrs={'placeholder': 'Select location'}),
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'expected_participants': forms.NumberInput(attrs={'placeholder': 'Enter expected participants'}),
        }

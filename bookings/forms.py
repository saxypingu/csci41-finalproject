from django import forms
from .models import Organizer, Contact_Person, Activity

# class OrganizerForm(forms.ModelForm):
#     class Meta:
#         model = Organizer
#         fields = ['name']

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'organizer_type', 'address']
        
class ContactPersonForm(forms.ModelForm):
    class Meta:
        model = Contact_Person
        fields = ['contact_email', 'contact_name', 'contact_phone']


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

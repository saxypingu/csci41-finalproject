from django import forms
from .models import Organizer, Activity_Details

# class OrganizerForm(forms.ModelForm):
#     class Meta:
#         model = Organizer
#         fields = ['name']

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'organizer_type', 'address', 'contact_email','contact_name','contact_phone']


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity_Details
        fields = ['name', 'location', 'date', 'start_time','end_time']
        widgets = {
            'organizer': forms.Select(attrs={'placeholder': 'Select organizer'}),
            'name': forms.TextInput(attrs={'placeholder': 'Enter activity name'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter activity location'}),
            'date': forms.DateInput(attrs={'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'start_time': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'end_time': forms.TimeInput(attrs={'placeholder': 'HH:MM', 'type': 'time'}),
            'expected_participants': forms.NumberInput(attrs={'placeholder': 'Enter expected participants'}),
        }

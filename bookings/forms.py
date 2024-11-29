from django import forms
from .models import Organizer

class OrganizerForm(forms.ModelForm):
    class Meta:
        model = Organizer
        fields = ['name', 'address', 'contact_person_name', 'contact_person_email', 'contact_person_phone', 'organizer_type']
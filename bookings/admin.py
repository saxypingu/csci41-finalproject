from django.contrib import admin

# Register your models here.
from .models import Organizer, Activity, Participant, Booking, ParticipantUser

admin.site.register(Organizer)
admin.site.register(Activity)
admin.site.register(Participant)
admin.site.register(Booking)
# admin.site.register(ParticipantUser)
# admin.site.register
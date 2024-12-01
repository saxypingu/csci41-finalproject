from django.contrib import admin

# Register your models here.
from .models import Organizer, Activity, Participant, Booking, NewUser

admin.site.register(Organizer)
admin.site.register(Activity)
admin.site.register(Participant)
admin.site.register(Booking)
admin.site.register(NewUser)


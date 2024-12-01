from django.contrib import admin

# Register your models here.
from .models import Organizer, Activity, Contact_Person, Participant, Booking
# from .models import NewUser

admin.site.register(Organizer)
admin.site.register(Activity)
admin.site.register(Contact_Person)
admin.site.register(Participant)
admin.site.register(Booking)
# admin.site.register(NewUser)


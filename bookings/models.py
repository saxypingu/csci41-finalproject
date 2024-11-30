from django.db import models

class Organizer(models.Model):
    # Defining custom id for the Organizer model; following conventions in specifications
    organizer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    TYPE_CHOICES = (
        ('external', 'External'),
        ('internal', 'Internal')
    )
    organizer_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    address = models.TextField()
    contact_email = models.ForeignKey('Contact_Person', related_name='organizer', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Contact_Person(models.Model):
    contact_name = models.CharField(max_length=128)
    contact_email = models.EmailField(max_length=128, unique=True)
    contact_phone = models.CharField(max_length=16, unique=True)

class Activity(models.Model):
    organizer = models.ForeignKey('Organizer', related_name='activities', on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    activity_number = models.AutoField(primary_key=True)
    LOCATIONS = (
        ('pridehall', 'Pridehall Theater'),
        ('innovatech', 'Innovatech Lecture Hall'),
        ('107', 'Room 107'),
        ('convergence', 'Convergence Center'),
    )
    location = models.CharField(max_length=256, choices=LOCATIONS)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    expected_participants = models.PositiveIntegerField()  # Expecting a positive number

    def __str__(self):
        return self.name 
    
    class Meta:
        unique_together = ['name', 'date', 'organizer']  # to avoid duplicates
    
class Participant(models.Model):
    PARTICIPANT_TYPES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('faculty', 'Faculty'),
    )
    id_number = models.CharField(max_length=6, unique=True) # Not sure if this should be unique; this would depend on how we implement the booking and participant creation. Will keep it unique for now.
    name = models.CharField(max_length=256)
    birth_date = models.DateField()
    department = models.CharField(max_length=256)
    participant_type = models.CharField(choices=PARTICIPANT_TYPES, max_length=32)

    def __str__(self):
        return self.name

# TODO: Insert extended models for Student, Faculty, and Staff here if we decide to do multi-table inheritance.



class Booking(models.Model):
    participant = models.ForeignKey(Participant, related_name='bookings', on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, related_name='bookings', on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.participant.name} - {self.activity.name}'

    class Meta:
        unique_together = ['participant', 'activity']  # Each participant can book an activity only once
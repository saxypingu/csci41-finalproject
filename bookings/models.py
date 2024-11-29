from django.db import models

class Organizer(models.Model):
    # Defining custom id for the Organizer model; following conventions in specifications
    organizer_id = models.AutoField(primary_key=True)
    name = models.ForeignKey('Organizer_Details', on_delete=models.CASCADE, related_name='orgname')
    
    contact_id = models.ForeignKey('Contact_Person', on_delete=models.CASCADE, related_name='contact')
    
    def __str__(self):
        return self.name
    
class Organizer_Details(models.Model):
    name = models.CharField(max_length=200)
    TYPE_CHOICES = (
        ('external', 'External'),
        ('internal', 'Internal')
    )
    organizer_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    address = models.TextField()

class Contact_Details(models.Model):
    contact_email = models.EmailField(unique=True, primary_key=True)
    contact_name = models.CharField(max_length=100)
    contact_person_phone = models.CharField(max_length=15, unique=True)
    
class Contact_Person(models.Model):
    # ideally, this should automatically create when making an organizer instance
    # but i forgor how
    contact_id = models.AutoField(primary_key=True)
    contact_email = models.ForeignKey('Contact_Details', on_delete=models.CASCADE, related_name='contactem')
    organizer = models.ForeignKey('Organizer', on_delete=models.CASCADE, related_name='contactorg')

class Activity(models.Model):
    organizer = models.ForeignKey('Organizer', related_name='activities', on_delete=models.CASCADE)
    name = models.ForeignKey('Activity_Details', related_name='actname', on_delete=models.CASCADE)
    activity_number = models.AutoField(primary_key=True)
    expected_participants = models.PositiveIntegerField()  # Expecting a positive number

    def __str__(self):
        return self.name 
    
    class Meta:
        unique_together = ['name', 'date', 'organizer']  # to avoid duplicates

class Activity_Details(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
class Participant(models.Model):
    PARTICIPANT_TYPES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('faculty', 'Faculty'),
    )
    id_number = models.CharField(max_length=6, unique=True) # Not sure if this should be unique; this would depend on how we implement the booking and participant creation. Will keep it unique for now.
    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    department = models.CharField(max_length=200)
    participant_type = models.CharField(choices=PARTICIPANT_TYPES, max_length=20)

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
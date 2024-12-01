from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
class Organizer(models.Model):
    # Defining custom id for the Organizer model; following conventions in specifications
    organizer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    contact_person_name = models.CharField(max_length=100)
    contact_person_email = models.EmailField(unique=True)
    contact_person_phone = models.CharField(max_length=15, unique=True)
    organizer_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Activity(models.Model):
    organizer = models.ForeignKey(Organizer, related_name='activities', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
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

class CustomAccountManager(BaseUserManager):

    def create_user(self, id_number, name, birth_date, participant_type, password, **other_fields):
        user = self.model(id_number=id_number, name=name, birth_date=birth_date, participant_type=participant_type, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, id_number, name, birth_date, participant_type, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(id_number, name, birth_date, participant_type, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    
    id_number = models.CharField(max_length=6, unique=True, primary_key=True)

    PARTICIPANT_TYPES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('faculty', 'Faculty'),
    )

    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    department = models.CharField(max_length=200)
    participant_type = models.CharField(choices=PARTICIPANT_TYPES, max_length=20)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'id_number' # Let the ID number be the user's username and primary key.
    REQUIRED_FIELDS = ['name', 'birth_date', 'department', 'participant_type']

    def __str__(self):
        return self.name + ' (' + self.participant_type + ')'
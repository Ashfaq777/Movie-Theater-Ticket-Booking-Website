import datetime
from email.policy import default
from tkinter import CASCADE
from xml.dom import ValidationErr
from django.core.exceptions import ValidationError
from django.db import models
from multiselectfield import MultiSelectField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms.widgets import NumberInput

# Create your models here.
class Theater(models.Model):
    
    theater_name = models.CharField(max_length=255, null= True)
    
    def __str__(self):
        return f"{self.theater_name}"
        
class Movie(models.Model):
    title = models.CharField(max_length=255,null=True)
    description = models.CharField(max_length=255,null=True)
    release_date=models.CharField(max_length=100, null=True)
    cover = models.ImageField(upload_to='movie_covers')
    ticket_price=models.IntegerField(default=300)
    booked_seats = models.ManyToManyField('Seat',blank=True)

    theater = models.ForeignKey(Theater, null=True, blank=True, on_delete=models.SET_NULL)
    #theater_select = models.ManyToManyField(Theater, blank=True)
    def __str__(self):
        return f"{self.title,self.theater,self.ticket_price}"


class Seat(models.Model):
    seat_no=models.IntegerField()
    customer_name=models.CharField(max_length=255)     
        
    customer_email=models.EmailField(max_length=555)     
    purchase_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_name} seat_no {self.seat_no}"

class ShowTime(models.Model):
    time_choices = (('10:00 AM', '10:00 AM'),
              ('12:00 PM', '12:00 PM'),
              ('2:00 PM', '2:00 PM'),
              ('4:00 PM', '4:00 PM'),
              ('6:30 PM', '6:00 PM'))



    
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.SET_NULL)
    time = MultiSelectField(choices=time_choices)  

    def __str__(self):
        return f"{ self.movie, self.time}"

class BookedSeats(models.Model):
    movie_name=models.ForeignKey(Movie, on_delete=models.SET_NULL,null=True, blank=True)
    showtime = models.ForeignKey(ShowTime, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return f"{self.movie_name, self.showtime}"

class bookedtickets(models.Model):
    def validate_date(date):
        if date < datetime.datetime.now().date():
            raise ValidationError("Date cannot be in the past")
    time_choices=(
        ('1','10:00 AM'),
        ('2','12:00 PM'),
        ('3','2:00 PM'),
        ('4','4:00 PM'),

    )   
    username = models.CharField(max_length=255)
    movie_name= models.CharField(max_length=255)
    number_of_tickets=models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)])
    selected_time=models.CharField(max_length=255, choices=time_choices, default='1',null=True)
    booking_date=models.DateField(validators=[validate_date])
    total_price= models.IntegerField(default=0)
    def __str__(self):
        return f"{self.username,self.movie_name,self.number_of_tickets,self.booking_date,self.selected_time,self.total_price}"

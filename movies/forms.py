from django import forms
from django.shortcuts import render, get_object_or_404
from django.forms.widgets import NumberInput
from django.shortcuts import render,redirect, get_object_or_404
from .models import BookedSeats, Movie, Theater, ShowTime
from django.core.exceptions import ValidationError
import datetime
class bookticketForm(forms.ModelForm):
    def validate_date(date):
        if date < datetime.datetime.now().date():
            raise ValidationError("Date cannot be in the past")

    number_of_tickets =forms.IntegerField(max_value=10,required=True)
    booking_date = forms.DateField(label='booking_date',widget=NumberInput(attrs={'type': 'date'}),required=True,validators=[validate_date])
    
    class Meta:
        model = BookedSeats
        fields = ('number_of_tickets','booking_date','time')

    # def __init__(self, time_choices, *args, **kwargs):
    #     super(bookticketForm,self,).__init__(*args,**kwargs)
    #     print('testing case 1',time_choices)
    #     self.fields['time'].choices = time_choices
        
    time_choices=(
        ('1','10:00 AM'),
        ('2','12:00 PM'),
        ('3','2:00 PM'),
        ('4','4:00 PM'),

    )   
    time = forms.ChoiceField(choices=time_choices, required=True)
      
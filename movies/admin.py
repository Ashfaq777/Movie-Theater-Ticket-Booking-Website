from django.contrib import admin
from .models import Movie, Theater, ShowTime, BookedSeats, bookedtickets
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title','description','release_date','theater','cover')


class TheaterAdmin(admin.ModelAdmin):
    list_display = ('theater_name',)


class ShowTimeAdmin(admin.ModelAdmin):
    list_display = ('movie','time',)   

class BookedSeatsAdmin(admin.ModelAdmin):
    list_display= ('movie_name','showtime',) 

class BookedticketsAdmin(admin.ModelAdmin):
    list_display= ('username','movie_name','number_of_tickets','selected_time','booking_date','total_price') 

admin.site.register(Movie, MovieAdmin)
admin.site.register(Theater, TheaterAdmin)
admin.site.register(ShowTime, ShowTimeAdmin)
admin.site.register(BookedSeats,BookedSeatsAdmin)
admin.site.register(bookedtickets,BookedticketsAdmin)
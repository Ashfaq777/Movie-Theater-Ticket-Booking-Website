from django.urls import path
from . import views


urlpatterns = [
   
    path('bookingform/<int:th_id>',views.booking, name='booking_page'),
    path('choose_theater/',views.chooseTheater, name='choose_theater'),
    path('ajax/load-showtimes/', views.load_showtimes, name='ajax_load_showtimes'), # AJAX
    path('buyticket/<int:movie_id>',views.bookingform, name='bookingform'),
]
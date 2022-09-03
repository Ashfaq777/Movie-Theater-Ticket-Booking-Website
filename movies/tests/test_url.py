from django.test import TestCase
from django.urls import reverse, resolve
from movies.views import booking, chooseTheater, bookingform
from movies.models import Theater, Movie
class TestUrls(TestCase):
    
    def test_booking_page_url_is_resolved(self):
        self.theater = Theater.objects.create(

            theater_name='testing'
        )
        url = reverse('booking_page',args=[self.theater.pk])
        self.assertEquals(resolve(url).func, booking)

    def test_choose_theater_url_is_resolved(self):
          
            url = reverse('choose_theater')
            self.assertEquals(resolve(url).func, chooseTheater)

    def test_booking_form_url_is_resolved(self):
                self.movies = Movie.objects.create(

                    title='testing'
                )
                url = reverse('bookingform', args=[self.movies.pk])
                self.assertEquals(resolve(url).func, bookingform)            
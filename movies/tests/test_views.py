from urllib import response
from django.test import TestCase, Client
from django.urls import reverse
from movies.models import Theater, Movie, ShowTime, bookedtickets


class TestViews(TestCase):

    def setUp(self):
        self.client= Client()
        self.theater = Theater.objects.create(

            theater_name='testing'
        )
        self.booking_url = reverse('booking_page',args=[self.theater.pk])

        self.choose_theater_url = reverse('choose_theater')
        

    def test_booking_GET(self):
        
        
        response = self.client.get(self.booking_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'movies/test.html')

    def test_choose_theater_GET(self):
            
            
            response = self.client.get(self.choose_theater_url)

            self.assertEquals(response.status_code, 200)
            self.assertTemplateUsed(response, 'movies/choose_theater.html')        

 
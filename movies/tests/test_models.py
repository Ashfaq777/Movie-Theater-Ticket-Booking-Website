from django.test import TestCase
from movies.models import Movie, Theater, bookedtickets

class TestModels(TestCase):

    def setUp(self):
        self.theater1 = Theater.objects.create(
            theater_name= 'theater test 1'
        )
        self.theater2 = Theater.objects.create(
            theater_name= 'theater test 2'
        )
    
    def test_create_theater(self):

        

        self.assertEquals(self.theater1.theater_name, 'theater test 1')

    def test_create_movie(self):



        self.movie1 = Movie.objects.create(
            title = 'spiderman no way home',
            description = 'dont mess with time',
            release_date = 10/20/2021,
            ticket_price = 300,
            theater = self.theater1
        )

        self.assertEquals(self.movie1.title, 'spiderman no way home')    
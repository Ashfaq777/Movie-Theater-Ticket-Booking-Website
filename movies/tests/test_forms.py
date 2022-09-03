from django.test import TestCase
from movies.forms import bookticketForm
from movies.models import bookedtickets

class TestForms(TestCase):

    def test_booked_ticket_form_valid(self):
      
        form = bookticketForm( data ={

            'number_of_tickets' : 4,
            'booking_date': "2022-10-22",
            'time': '1'


        })
        # print("Checking ERRORS!:",form.errors)
        self.assertTrue(form.is_valid())

    def test_booked_ticket_form_no_data(self):
        form = bookticketForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 3)





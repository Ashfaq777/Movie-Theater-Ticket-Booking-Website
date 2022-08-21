from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Theater, BookedSeats, ShowTime,bookedtickets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import FormView
from django.http.response import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import bookticketForm
import nltk
from nltk import flatten



# Create your views here.
def booking (request, th_id):
    theater= get_object_or_404(Theater, pk = th_id)
    
    movie_list= Movie.objects.filter(theater=theater)
    
    form = bookticketForm(request.POST)
   
    
    return render(request,'movies/test.html',{"movies": movie_list, 'form': form})

def chooseTheater(request):
    theater_list= Theater.objects.all()
    print('theaters check: ',theater_list)
    return render(request, 'movies/choose_theater.html',{"theaters":theater_list})   


def load_showtimes(request):
    movie_id = request.GET.get('movie_id')
    print("test check 1",movie_id)
    showtimes = ShowTime.objects.filter(movie_id=movie_id).all()
    print("test check 2",showtimes.values('time'))
    time_list=showtimes.values('time')
    t= time_list.values_list('time')
    t=list(t)
    t=list(t[0])
    t=flatten(t)
    print('time check', t)
    showtimes=t
    return render(request, 'movies/showtimes_dropdown_list_options.html', {'showtimes': showtimes})
@csrf_exempt
@login_required
def bookingform(request, movie_id):
    
            
        
            # movie= get_object_or_404(Movie, pk = movie_id)
    
            # showtime_list= ShowTime.objects.filter(movie=movie)
            # time_list=showtime_list.values('time')
            # t= time_list.values_list('time')
            # st=t
            # t=list(t)
            # print("t is ",t)
            # t=list(t[0])
            # print("t is ",t)
            # t=flatten(t)
            # test_list=[]
            # count=1
            # for i in t:
            #     test_list.append( (str(count),i) )
            #     count=count+1
            # print("test list is ",test_list)
            
            # form = bookticketForm(test_list)
            # print(form.is_valid())
            # print(form.errors)
            if request.method=='POST':
                form = bookticketForm(request.POST)
                print("i am here 1")
                if form.is_valid():
                    print("i am here 2")
                    customer=request.user

                    #print("movie_id is ",movie_id)
                    movie= get_object_or_404(Movie, pk = movie_id)
                    selected_movie=movie.title

                    num_of_tickets = form.cleaned_data.get('number_of_tickets')
                    chosen_time = form.cleaned_data.get('time')
                    print('test time is',chosen_time)
                    book_date= form.cleaned_data.get('booking_date')
                    totalprice=movie.ticket_price * num_of_tickets
                    print("total price is ",totalprice)
                    ticket = bookedtickets.objects.create(username=customer,movie_name=selected_movie,number_of_tickets=num_of_tickets,selected_time=chosen_time, booking_date=book_date,total_price=totalprice )
                    print('ticket is ',ticket)
                    return redirect('tickets')
            else:
                form = bookticketForm()
             
               
            return render(request, 'movies/booking.html',{'form':form})

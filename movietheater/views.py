from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from movies.models import Theater, Movie, bookedtickets


# Create your views here.

def test(request):
    return render(request, 'movietheater/dashboard.html')
def dashboard(request):
    theater_list= Theater.objects.all()
    movie_list= Movie.objects.all()
    print("movies",movie_list)
    copy_list=[]
    copy_list.append(movie_list[0])
    print("copy list= ",copy_list)
    flag=False
    for i in movie_list:
        for j in copy_list:
            if i.title == j.title :
                flag=True
                break
        if flag==False:
            copy_list.append(i)
        flag=False    
    print("new copy list",copy_list)
    movie_list=copy_list
    return render(request, 'movietheater/index.html', {"theaters":theater_list, "movies":movie_list})


def theater(request):
    theater_list= Theater.objects.all()
    movie_list= Movie.objects.all()
    print("movies",movie_list)
    copy_list=[]
    copy_list.append(movie_list[0])
    print("copy list= ",copy_list)
    flag=False
    for i in movie_list:
        for j in copy_list:
            if i.title == j.title :
                flag=True
                break
        if flag==False:
            copy_list.append(i)
        flag=False    
    print("new copy list",copy_list)
    movie_list=copy_list
    
    return render(request, 'movietheater/showtimes.html',{"theaters":theater_list, "movies":movie_list}    )

def showmovies(request, theater_id):
    theater_list= Theater.objects.all()
    theater= get_object_or_404(Theater, pk = theater_id)
    print("theater is :",theater)
    movie_list= Movie.objects.filter(theater=theater)
    print("movie list :",movie_list)
    return render(request, 'movies/movie_list.html',{"theaters":theater_list,"movies":movie_list})

def showticket(request):
    theater_list= Theater.objects.all()
    ticket_list=bookedtickets.objects.filter(username=request.user)
    print("tickets of user",ticket_list)

    return render(request, 'movietheater/bookedtickets.html',{"theaters":theater_list,"tickets":ticket_list})
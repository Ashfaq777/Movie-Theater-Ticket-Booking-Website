from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.dashboard, name='index'),
    path('movietheater/', views.theater, name='theaters'),
    path('tester/', views.test),
    path('<int:theater_id>',views.showmovies,name='movies'),
    path('bookedtickets/',views.showticket,name="tickets"),

]
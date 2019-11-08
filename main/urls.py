from django.urls import path
from main import views


urlpatterns = [
    path('', views.home),
    path('signup/', views.signup),
    path('login/', views.log_in, name='log-in'),
    path('contactus/', views.contactus, name='contactus'),
    path('logout/', views.log_out , name='log-out'),
    path('profile/', views.profile, name='profile'),

]

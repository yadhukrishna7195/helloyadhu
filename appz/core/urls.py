from .views import *
from django.urls import path
urlpatterns = [

path('',home,name='home'),
path('about/',about,name='about'),
path('skills/',skills,name='skills'),
path('contact/',contact,name='contact'),




]
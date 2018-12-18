from django.conf.urls import  url
from food import views

urlpatterns =[ 
        url(r'^$',views.index2, name='index2'),
        url(r'^index2/',views.index2, name='index2'),
          ] 

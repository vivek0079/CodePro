from django.conf.urls import url

from .views import registerUser, loginUser, logoutUser, savetoProfile, removefromProfile, viewProfile


app_name = 'authenticate'

urlpatterns = [
    url(r'^$', viewProfile, name='view-profile'),
    url(r'^save/$', savetoProfile, name='save'),
    url(r'^remove/$', removefromProfile, name='remove'),
    
    url(r'^login/$', loginUser, name='login'),
    url(r'^register/$', registerUser, name='register'),
    url(r'^logout/$', logoutUser, name='logout'),
]
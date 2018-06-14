from django.conf.urls import url

from .views import registerUser, loginUser, logoutUser, removefromProfile, viewProfile, userExists


app_name = 'authenticate'

urlpatterns = [
    url(r'^$', viewProfile, name='view-profile'),
    url(r'^remove/$', removefromProfile, name='remove'),
    
    url(r'^login/$', loginUser, name='login'),
    url(r'^register/$', registerUser, name='register'),
    url(r'^logout/$', logoutUser, name='logout'),
    
    url(r'^validate/$', userExists, name='validate')
]
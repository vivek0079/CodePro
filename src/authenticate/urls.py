from django.conf.urls import url

from .views import registerUser, loginUser, logoutUser, userExists

app_name = 'authenticate'

urlpatterns = [    
    url(r'^login/$', loginUser, name='login'),
    url(r'^register/$', registerUser, name='register'),
    url(r'^logout/$', logoutUser, name='logout'),
    
    url(r'^validate/$', userExists, name='validate')
]
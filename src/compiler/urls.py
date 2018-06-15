from django.conf.urls import url, include

from .views import index, executeCode, saveCode, profile, deleteCode, viewSavedCode, checkConnection

app_name = 'compiler'

urlpatterns = [
    url(r'^$', index, name='index'),
    
    # Code execution URL
    url(r'^execute/$', executeCode, name='execute'),

    # Profile related URLs
    url(r'^profile/$', profile, name='profile'),
    url(r'^save/$', saveCode, name='save'),
    url(r'^delete/$', deleteCode, name='delete'),    
    url(r'^viewcode/$', viewSavedCode, name='code-view'),

    # Utility checker URL
    url(r'^checker/$', checkConnection, name='connec-check')
]
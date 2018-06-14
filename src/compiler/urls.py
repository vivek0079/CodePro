from django.conf.urls import url, include

from .views import index, executeCode, saveCode, profile, deleteCode, viewSavedCode

app_name = 'compiler'

urlpatterns = [
    url(r'^$', index, name='index'),
    
    url(r'^execute/$', executeCode, name='execute'),
    url(r'^profile/$', profile, name='profile'),

    url(r'^save/$', saveCode, name='save'),
    url(r'^delete/$', deleteCode, name='delete'),    
    url(r'^viewcode/$', viewSavedCode, name='code-view'),
]
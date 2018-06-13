from django.conf.urls import url, include

from .views import index, executeCode, runCode, viewSavedCode

app_name = 'compiler'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^execute/$', executeCode, name='execute'),
    url(r'^code/(?P<code_id>[\w{}.-])/$', viewSavedCode, name='code-view'),
]
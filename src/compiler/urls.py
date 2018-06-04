from django.conf.urls import url, include

from .views import index, compileCode, runCode, viewSavedCode

app_name = 'compiler'

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^compile/$', compileCode, name='compile'),
    url(r'^run/$', runCode, name='run'),
    url(r'^code/(?P<code_id>[\w{}.-])/$', viewSavedCode, name='code-view'),
]
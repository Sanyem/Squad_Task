from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views

app_name = 'game'

urlpatterns=[
url(r'^play/$', views.play, name='play'),
]
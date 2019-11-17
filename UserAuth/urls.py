from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views
app_name = 'UserAuth'

urlpatterns=[
url(r'^signup/(?P<message>.*)$', views.signup, name='signup'),
url(r'^user_login/(?P<message>.*)$', views.user_login, name='user_login'),
url(r'^logout$', views.logout, name='logout'),
url(r'^$', views.home, name='home'),
url(r'^profile/$', views.profile, name='profile'),
]
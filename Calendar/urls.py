from django.conf.urls import patterns, include, url

from Calendar import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^event/edit/$', views.edit_event, name='edit_event')
)

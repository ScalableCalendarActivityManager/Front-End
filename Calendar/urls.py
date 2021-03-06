from django.conf.urls import patterns, include, url

from Calendar import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^signin/$', views.signin, name='signin'),
    url(r'^signout/$', views.signout, name='signout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^event/edit/$', views.edit_event, name='edit_event'),
    url(r'^calendar/add/$', views.add_to_calendar, name='add_to_calendar'),
    url(r'^calendar/newc/$', views.new_calendar, name='new_calendar'),
    url(r'^calendar/newe/$', views.new_event, name='new_event'),
    url(r'^calendar/dele/$', views.del_event, name='del_event'),
    url(r'^calendar/viewers/(?P<cid>[0-9]+)/(?P<cname>\w+)/$', views.cal_viewers, name='cal_viewers'),
    url(r'^valendar/delv/$', views.del_viewer, name='del_viewer')
)

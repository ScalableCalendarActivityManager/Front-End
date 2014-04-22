from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SCAM.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include('Calendar.urls', namespace='Calendar')),

    url(r'^admin/', include(admin.site.urls)),
)

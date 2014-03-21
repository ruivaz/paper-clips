from django.conf.urls import patterns, include, url
from whapsat.views import hello, current_time, hours_ahead 
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'whapsat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^hello/$', hello),
    url(r'^time/$', current_time),
    url(r'time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^admin/', include(admin.site.urls)),
)

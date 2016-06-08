from django.conf.urls.defaults import patterns, include, url
#from django.contrib import admin

#admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    (r'^pm/go/(?P<state>[a-zA-Z_]\w*)/$', 'WebService.views.pm_go'),
    (r'^pm/go/$', 'WebService.views.pm_go'),
    (r'^pm/verify/(?P<state>[a-zA-Z_]\w*)/$', 'WebService.views.pm_verify'),
    (r'^pm/verify/$', 'WebService.views.pm_verify'),
)

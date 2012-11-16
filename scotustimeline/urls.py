from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scotustimeline.views.home', name='home'),
    # url(r'^scotustimeline/', include('scotustimeline.foo.urls')),

    # homepage
    (r'^$', 'timeline.views.index',),

    url(r'^category/(?P<slug>[^\.]+)', 'timeline.views.category', name = 'category'),

#    url('r^category-list/'

    url('r^justice/(?P<slug>[^\.]+)', 'timeline.views.justice', name = 'justice'),

#    url('r^justice-list/'

    url('r^case/(?P<slug>[^\.]+)', 'timeline.views.justice', name = 'case'),

#    url('r^case-list/'

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('timeline.views',
    # Examples:
    # url(r'^$', 'scotustimeline.views.home', name='home'),
    # url(r'^scotustimeline/', include('scotustimeline.foo.urls')),

    # homepage
    url(r'^$', 'index', name = 'home'),

    url(r'^category-list/', 'category_list', name = 'category_list'),

    # url('r^category/'

    url(r'^justice-list/', 'justice_list', name = 'justice_list'),

    # url('r^justice/'

    url(r'^case-list/', 'case_list', name = 'case_list'),

    # url('r^case/'

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

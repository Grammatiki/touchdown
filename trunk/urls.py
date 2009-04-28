from django.conf.urls.defaults import *
from django.contrib.gis import admin
# Uncomment the next two lines to enable the admin:

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^touchdown/', include('touchdown.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^game/(?P<game_name>[^/]*)/?$','referee.views.game_map'),
    (r'^openid/', include('django_openid_auth.urls')),
)
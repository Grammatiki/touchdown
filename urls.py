from django.conf.urls.defaults import *
from django.contrib.gis import admin
from referee import models, forms
import settings
# Uncomment the next two lines to enable the admin:

#admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^touchdown/', include('touchdown.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root) ,
    
    url(r'^$','referee.views.index',name='index'),

    url(r'^game/(?P<game_name>[^/]*)/?$','referee.views.game', name='game'),

    url(r'^new_game/?$',
        'django.views.generic.create_update.create_object',
        {'form_class':forms.GameForm}, name='new_game'),
        
    url(r'^touchdown/(?P<object_id>\d+)/?$',
        'django.views.generic.list_detail.object_detail',
        {'queryset':models.Touchdown.objects.all()}, name='touchdown'),

    (r'^claim_touchdown/?$',
        'django.views.generic.create_update.create_object',
        {'model':models.Touchdown, 'login_required':True}),

    (r'^openid/', include('django_openid_auth.urls')),

    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),    
)

from django.conf import settings
from django.contrib.gis import admin
from referee.models import GamePoint, Game
from referee.admin import GameAdmin
from django import forms

# Getting an instance so we can generate the map widget; also
# getting the geometry field for the model.
admin_instance = GameAdmin(Game, admin.site)
nw_field = Game._meta.get_field('northwest_corner')
se_field = Game._meta.get_field('southeast_corner')

# Generating the widget.
nwWidget = admin_instance.get_map_widget(nw_field)
seWidget = admin_instance.get_map_widget(se_field)

class GameForm(forms.ModelForm):
    """
    A ModelForm for creating new games. We can't use a default generic view modelform
    because we want a geodjango admin map widget in there and that has to be done
    manually.
    
    To get the map widget in there, I followed instructions at:
    http://yml-blog.blogspot.com/2009/01/how-to-use-same-widget-than-geodjango.html
    """
    
    northwest_corner = forms.CharField(widget=nwWidget())
    southeast_corner = forms.CharField(widget=seWidget())
    class Meta:
        model = Game
        exclude = ("content_type","object_id","player")
    class Media:
        js = ("http://openlayers.org/api/2.6/OpenLayers.js",)
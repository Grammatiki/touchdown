#Things that need to be installed for touchdown to work.

# Touchdown dependencies #

Users playing the game need no software except a browser.

To run a touchdown server, the following are required:
  * [Django](http://www.djangoproject.com) and its dependancies
  * Dependencies for geodjango (now merged into django as django.gis). This includes the GEOS library. Touchdown can be used with a MySQL backend, in which case you do not need proj4. note: check on proj4 and also GDAL
  * django-openid-auth for openid logins
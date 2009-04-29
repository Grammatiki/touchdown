from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.gis.geos import Point, MultiPoint
import random
#import pointgen

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    body = models.TextField()

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    openid=models.ForeignKey(User)

class GamePoint(models.Model):
    point = models.PointField()
    game = models.ForeignKey('Game')
    objects = models.GeoManager()    
    
    def count_winners(self):
        return GamePoint.Touchdowns_set.count()
    
    def __unicode__(self):
        return self.game.name + ' ' + str(self.pk)

class Game(models.Model):
    name=models.CharField(max_length=50, unique=True)
    description=models.TextField(blank=True,null=True)
    northwest_corner=models.PointField()
    southeast_corner=models.PointField()
    objects = models.GeoManager()
    start_date = models.DateTimeField(default=datetime.now())
    end_date = models.DateTimeField()
    player = models.ManyToManyField(Person, blank=True, null=True)
    motorized_vehicles_allowed = models.BooleanField(default=True)
    
    def time_left(self):
        res=datetime.now()-self.end_date
        if res>0: #this doesn't work, fix it.
            return unicode(res)
        else:
            return False

    def time_until(self):
        res=self.start_date-datetime.now()
        if res>0: #this doesn't work, fix it.
            return unicode(res)
        else:
            return False
    
    def __unicode__(self):
        return self.name    
    
    def get_absolute_url(self):
        return settings.URL_ROOT + reverse('game',args=[self.name])

    def make_point_set(game, pointCount):
        """Given a Game, produces a set of pointCount GamePoints each linked to
        it via a foreignkey and saves it in the database."""

        points=[]
        for point in range(pointCount):
            xCoord=random.uniform(game.northwest_corner.x, game.southeast_corner.x)
            yCoord=random.uniform(game.northwest_corner.y, game.southeast_corner.y)
            newgp=GamePoint(point=Point(xCoord,yCoord), game=game)
            newgp.save()

    def save(self, *args, **kw):
        super(Game, self).save(*args, **kw)
        make_point_set(game=self, pointCount=50)
        super(Game, self).save(*args, **kw)

# This is a really weird place for this function. Please try and put it somewhere better. Beware
# circular dependency problems.
def make_point_set(game, pointCount):
    """Given a Game, produces a set of pointCount GamePoints each linked to
    it via a foreignkey and saves it in the database."""

    points=[]
    for point in range(pointCount):
        xCoord=random.uniform(game.northwest_corner.x, game.southeast_corner.x)
        yCoord=random.uniform(game.northwest_corner.y, game.southeast_corner.y)
        newgp=GamePoint(point=Point(xCoord,yCoord), game=game)
        newgp.save()


class Touchdown(models.Model):
    point = models.ForeignKey(GamePoint)
    player = models.ForeignKey(User)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    proof_photo = models.ImageField(upload_to='proof_photo', blank=True, null=True)
    approved = models.BooleanField(default=False)
    def __unicode__(self):
        return unicode(self.point) + ' ' + self.player.username + ' ' +unicode(self.date)
    def get_absolute_url(self):
        #return settings.URL_ROOT + "/expedition/%s" % self.year
        return settings.URL_ROOT + reverse('touchdown',args=[self.pk])        

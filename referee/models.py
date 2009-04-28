from django.contrib.gis.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    body = models.TextField()

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    openid=models.ForeignKey(User)

class Game(models.Model):
    name=models.CharField(max_length=50, unique=True)
    northwest_corner=models.PointField()
    southeast_corner=models.PointField()
    objects = models.GeoManager()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    player = models.ManyToManyField(Person, blank=True, null=True)
    
    def time_left(self):
        res=self.end_date-datetime.now()
        if res>0:
            return unicode(res)
        else:
            return False

    def time_until(self):
        res=self.start_date-datetime.now()
        if res>0:
            return unicode(res)
        else:
            return False
    
    def __unicode__(self):
        return self.name    

class GamePointSet(models.Model):
    game = models.OneToOneField(Game)
    objects = models.GeoManager()
    points = models.MultiPointField(null=True, blank=True)
    def __unicode__(self):
        return self.game.name

class GamePoint(models.Model):
    point = models.PointField()
    game = models.ForeignKey(Game)
    objects = models.GeoManager()    
    
    def count_winners(self):
        return GamePoint.Touchdowns_set.count()
    
    def __unicode__(self):
        return self.game.name + ' ' + str(self.pk)

class Touchdown(models.Model):
    point = models.ForeignKey(GamePoint)
    player = models.ForeignKey(User)
    date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    proof_photo = models.ImageField(upload_to='proof_photo')
    def __unicode__(self):
        return unicode(self.point) + ' ' + self.player.username + ' ' +unicode(self.date)

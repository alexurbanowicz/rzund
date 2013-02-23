from django.db import models

# Create your models here.

class Person (models.Model):

  firstname   = models.TextField (empty=False)
  lastname    = models.TextField (empty=False)
  middlenames = models.TextField (empty=True)
  birth       = models.DateField ()
  death       = models.DateField (empty=True)
  biogram     = models.TextField ()

class Tag (models.Model):
  class name = models.TextField() 

class Organization (models.Model):
  name = models.TextField (empty=False)

class Affiliation (models.Model):
  person       = models.ForignKeyField (Person)
  organization = models.ForeignKey (Organization)
  tag          = models.ForignKeyField (Tag)
  start        = models.DateTimeField ()
  end          = models.DateTimeField (empty=True)

class Event (models.Model):

  start = models.ManyToManyField(Person)
  description = models.TextField ()


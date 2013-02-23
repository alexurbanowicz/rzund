from django.db import models

# Create your models here.

class Person (models.Model):

  firstname   = models.TextField ()
  lastname    = models.TextField ()
  middlenames = models.TextField (blank=True)
  birth       = models.DateField (blank=True)
  death       = models.DateField (blank=True)
  biogram     = models.TextField (blank=True)


class Tag (models.Model):
  name = models.TextField() 


class Organization (models.Model):
  name = models.TextField ()


class Affiliation (models.Model):

  person       = models.ForeignKey (Person)
  organization = models.ForeignKey (Organization)
  tag          = models.ForeignKey (Tag)
  start        = models.DateTimeField ()
  end          = models.DateTimeField (blank=True)


class Event (models.Model):

  start       = models.DateField ()
  end         = models.DateField (blank=True)
  description = models.TextField ()
  persons     = models.ManyToManyField(Person) 


class Source (models.Model):

  title =       models.TextField ()
  description = models.TextField (blank=True)
  url =         models.URLField (blank=True)
  file =        models.FileField (upload_to='sources/%s', blank=True)

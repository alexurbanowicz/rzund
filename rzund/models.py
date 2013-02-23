from django.db import models

# Create your models here.

class Person (models.Model):

  firstname   = models.TextField ()
  lastname    = models.TextField ()
  middlenames = models.TextField (blank=True)
  birth       = models.DateField (blank=True, null=True)
  death       = models.DateField (blank=True, null=True)
  biogram     = models.TextField (blank=True)
 # photo       = models.ImageField (blank=True,upload_to='static')

  def __unicode__ (self):
    return ' '.join((self.firstname,self.lastname))


class Tag (models.Model):
  name = models.TextField() 

  def __unicode__ (self):

    return self.name


class Organization (models.Model):
  name = models.TextField ()
#  acronym = models.TextField ()
  def __unicode__ (self):
    return self.name

class Position (models.Model):
  'affiliation type - prezydent, premier, minister'

  name = models.TextField (blank=False) 

  def __unicode__ (self):

    return self.name


class Affiliation (models.Model):

  position     = models.ForeignKey (Position)
  person       = models.ForeignKey (Person)
  organization = models.ForeignKey (Organization)
  tag          = models.ForeignKey (Tag)
  start        = models.DateField (blank=True, null=True)
  end          = models.DateField (blank=True, null=True)

  def __unicode__ (self):

    return self.person.firstname + self.person.lastname + self.position.name
  

class Event (models.Model):

  start       = models.DateField (blank=True, null=True)
  end         = models.DateField (blank=True, null=True)
  name        = models.TextField ()
  description = models.TextField (blank=True)
  persons     = models.ManyToManyField(Person) 

  def __unicode__ (self): 

    return self.start + self.description


class Source (models.Model):

  title =       models.TextField ()
  description = models.TextField (blank=True)
  url =         models.URLField (blank=True)
  file =        models.FileField (upload_to='sources/%s', blank=True)

  def __unicode__ (self):

    return self.title

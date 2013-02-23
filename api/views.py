# Create your views here.

import datetime, json

from django.template import Context, loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse as HTTPResponse

from rzund.models import Tag, Person, Affiliation

def query (request, tag, date='now'):

  if date == 'now':
    date = datetime.datetime.now()

  tag = get_object_or_404 (Tag, name__exact=tag)

  affs = Affiliation.objects.filter(tag__exact=tag).filter(start__lte=date, end__gte=date)

  result = dict(persons=[ (a.person.id, str(a.person), a.position.name, a.organization.name) for a in affs ])

  return HTTPResponse (json.dumps(result))

  

# Create your views here.

import datetime, json

from django.template import Context, loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse as HTTPResponse
from django.db.models import Q

from rzund.models import Tag, Person, Affiliation

def query (request, tag, date='now'):

  if date == 'now':
    date = datetime.datetime.now()

  tag = get_object_or_404 (Tag, name__exact=tag)

  affs = Affiliation.objects.filter(tag__exact=tag).filter(Q(start__lte=date)|Q(start__exact=None)).filter(Q(end__gte=date)|Q(end__exact=None))

  result = dict(persons=[ (a.person.id, str(a.person), a.position.name, a.organization.name) for a in affs ])

  return HTTPResponse (json.dumps(result))

  

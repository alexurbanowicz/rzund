# Create your views here.

from django.template import Context, loader
from django.shortcuts import get_object_or_404
from django.http import HttpResponse as HTTPResponse

from models import Person, Affiliation


def person (request, object_id):

  person = get_object_or_404 (Person, pk=object_id)
  affils = Affiliation.objects.filter(person__exact=person)
  events = Event
  template = loader.get_template ("person.html")
  result = dict(person=person, affiliations=affils)

  return HTTPresponse (template.render(Context(result)))

  



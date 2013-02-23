from django.conf.urls.defaults import *

urlpatterns = patterns('',
# Example:
  (r'^tag/(?P<tag>\w+)/$', 'api.views.query'),
  (r'^tag/(?P<tag>\w+)/now/$', 'api.views.query'),
  (r'^tag/(?P<tag>\w+)/(?P<date>\d\d\d\d-\d\d?-\d\d?)/$', 'api.views.query'),
  (r'^person/(?P<object_id>\d+)/$', 'api.views.person'),
)


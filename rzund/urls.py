from django.conf.urls.defaults import *

urlpatterns = patterns('',
# Example:
  (r'^(?P<object_id>\d+)/$', 'rzund.views.person'),
)

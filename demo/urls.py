from django.conf.urls.defaults import *
from django.contrib import admin
from django.http import HttpResponse
from django.db import connection
from demo_models.models import Item
from pprint import pformat

admin.autodiscover()

def example(request):
    # The QuerySet items are decorated with additional properties
    #
    # In this case, it's obvious that the 'is_current' could be determined elsewhere too.
    # However, in more complex situations, this avoids having to pass the 'request' object
    # to the model layer just to get some attribute set that happens to be important for the template.
    #
    # There are off course, other situations to think of as well, where the QuerySet result
    # could include some information of variables you'd rather not pass down to the models.

    def add_prop(item):
        item.is_current = (item.get_absolute_url() == request.path)
    qs = Item.objects.all().decorate(add_prop)

    s = []
    for item in qs:
        s.append('Item "%s": is current? %s' % (item.get_absolute_url(), item.is_current))

    return HttpResponse(
        "<html><body><h1>Current path: '%s'</h1>" % request.path
        + "<p>Testing items:</p>\n"
        + '<br>'.join(s) + '<pre>%s</body></html>' % pformat(connection.queries)
    )


urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'', example),
)

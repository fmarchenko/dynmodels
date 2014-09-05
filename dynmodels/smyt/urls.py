from django.conf.urls import patterns, include, url
from smyt.views import FrontPage, GetDataView, SetDataView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = patterns('',
    url(r'^getData/(?P<model_class>.*)', GetDataView.as_view(), name='get_data'),
    url(r'^setData/(?P<model_class>.*)', csrf_exempt(SetDataView.as_view()), name='set_data'),
    url(r'^$', FrontPage.as_view(), name='frontpage'),
)
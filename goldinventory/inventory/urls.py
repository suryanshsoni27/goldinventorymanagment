from django.conf.urls import url
from .views import *

# sends call to url
urlpatterns = [
    url(r'^$', index, name='index'),

    url(r'^display_earrings$', display_earrings, name='display_earrings'),
    url(r'^display_rings$', display_earrings, name='display_rings'),
    url(r'^display_diamonds$', display_earrings, name='display_diamonds')


]

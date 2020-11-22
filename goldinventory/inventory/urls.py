from django.conf.urls import url
from .views import *

# sends call to url
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^display_earrings$', display_earrings, name='display_earrings'),
    url(r'^display_rings$', display_rings, name='display_rings'),
    url(r'^display_diamonds$', display_diamonds, name='display_diamonds'),
    url(r'^add_earing$', add_earrings, name='add_earrings'),
    url(r'^add_diamonds$', add_diamonds, name='add_diamonds'),
    url(r'^add_rings$', add_rings, name='add_rings'),
    url(r'^edit_earrings/(?P<id>\d+)$', edit_earrings, name='edit_earrings'),
    url(r'^edit_ring/(?P<id>\d+)s$', edit_rings, name='edit_rings'),
    url(r'^edit_diamonds/(?P<id>\d+)$', edit_diamonds, name='edit_diamonds'),
    url(r'^delete_diamonds/(?P<id>\d+)$',
        delete_diamonds, name='delete_diamonds'),
    url(r'^delete_rings/(?P<id>\d+)$', delete_rings, name='delete_rings'),
    url(r'^delete_earrings/(?P<id>\d+)$',
        delete_earrings, name='delete_earrings'),
]

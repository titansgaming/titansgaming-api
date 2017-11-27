from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from titansgaming.mumble.views import (
    MumbleView,
    MumbleServersListView,
    MumbleServersDetailView,
)


urlpatterns = [
    url(
        r'^$',
        MumbleView.as_view(),
        name='mumble-root',
    ),
    url(
        r'^servers/$',
        MumbleServersListView.as_view(),
        name='mumble-servers-list',
    ),
    url(
        r'^servers/(?P<pk>[0-9]+)/$',
        MumbleServersDetailView.as_view(),
        name='mumble-servers-detail',
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)

from django.conf.urls import url

from titansgaming.mumble.views import MumbleView

urlpatterns = [
    url(
        r'^$',
        MumbleView.as_view(),
        name='mumble_index'
    ),
]

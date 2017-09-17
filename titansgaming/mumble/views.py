import json
from requests import get

from django.conf import settings
from django.views.generic import TemplateView


def _process_channel(feed):
    channel = {
        'name': feed['name'],
        'description': feed['description'],
        'url': feed['x_connecturl'],
        'users': feed['users'],
        'channels': [],
    }
    if feed['channels']:
        for child in feed['channels']:
            channel['channels'].append(_process_channel(child))
    return channel


class MumbleView(TemplateView):
    template_name = "mumble/index.html"

    def _get_channels(self, feed):
        channels = _process_channel(feed['root'])
        import pprint
        pprint.pprint(channels)
        return channels

    def get_context_data(self, **kwargs):
        response = get(settings.MUMBLEBOXES_API)
        feed = json.loads(response.text)

        context = super().get_context_data(**kwargs)
        context['server_name'] = feed['name']
        context['server_url'] = feed['x_connecturl']
        context['channels'] = self._get_channels(feed)
        return context

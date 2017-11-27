import json

from django.conf import settings
from requests import get


def _process_channel(feed):
    channel = {
        'name': feed['name'],
        'description': feed['description'],
        'url': feed['x_connecturl'],
        'users': [],
        'channels': [],
    }
    if feed['channels']:
        for child in feed['channels']:
            channel['channels'].append(_process_channel(child))
    if feed['users']:
        for user in feed['users']:
            channel['users'].append(_process_user(user))
    return channel


def _process_user(user):
    return {
        'name': user['name'],
        'comment': user['comment'],
        'deaf': user['deaf'],
        'mute': user['mute'],
        'online_seconds': user['onlinesecs'],
        'idle_seconds': user['idlesecs'],
    }
    return user


class MumbleServer:
    def __init__(self, **kwargs):
        for field in ('id', 'name'):
            setattr(self, field, kwargs.get(field, None))
        self.pk = self.id

    def get_channel_list(self):
        response = get(settings.MUMBLEBOXES_API)
        feed = json.loads(response.text)
        channels = [_process_channel(feed['root'])]
        return channels


mumble_servers = {
    1: MumbleServer(id=1, name='Titans Gaming'),
}

from django.http import Http404
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView

from .models import mumble_servers
from .serializers import (
    MumbleServerSerializer,
    MumbleServerDetailSerializer,
)


class MumbleView(APIView):
    def get(self, request):
        return Response({
            'servers': reverse(
                'mumble-servers-list', request=request, format=None
            ),
        })


class MumbleServersListView(APIView):
    serializer_class = MumbleServerSerializer

    def get(self, request):
        serializer = MumbleServerSerializer(
            instance=mumble_servers.values(),
            many=True,
            context={'request': request},
        )
        return Response(serializer.data)


class MumbleServersDetailView(APIView):
    def get_object(self, pk):
        if int(pk) == 1:
            return mumble_servers[1]
        else:
            raise Http404

    def get(self, request, pk, format=None):
        mumble_server = self.get_object(pk)
        serializer = MumbleServerDetailSerializer(
            mumble_server,
            context={'request': request},
        )
        return Response(serializer.data)

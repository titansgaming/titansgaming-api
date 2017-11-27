from rest_framework import serializers

from .models import MumbleServer


class MumbleServerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    url = serializers.HyperlinkedIdentityField(
        view_name='mumble-servers-detail',
    )

    class Meta:
        model = MumbleServer
        fields = (
            'id',
            'name',
            'url',
        )


class MumbleServerDetailSerializer(MumbleServerSerializer):
    channels = serializers.SerializerMethodField()

    class Meta(MumbleServerSerializer.Meta):
        fields = MumbleServerSerializer.Meta.fields + ('channels',)

    def get_channels(self, server):
        return server.get_channel_list()

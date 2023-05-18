from rest_framework import serializers

from demo.models import Avs


class AvsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Avs
        fields = ['id', 'user', 'text', 'created_at', 'open']
        read_only_fields = ['user']#поля для чтения
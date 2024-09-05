from rest_framework import serializers
from api.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class DLOSerializer(serializers.Serializer):
    url = serializers.URLField()

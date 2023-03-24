from rest_framework import serializers

from main.user.models import User
from main.abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):
    class Meta:
        model = User
        # List of all the fields that can be included in a request or a response
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "bio",
            "avatar",
            "email",
            "is_active",
            "created",
            "updated",
        ]
        # List of all the fields that can only be read by the user
        read_only_field = ["is_active"]

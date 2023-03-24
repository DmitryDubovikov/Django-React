from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from main.abstract.serializers import AbstractSerializer
from main.user.serializers import UserSerializer
from main.post.models import Post
from main.user.models import User


class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(
        queryset=User.objects.all(), slug_field="public_id"
    )

    def validate_author(self, value):
        if self.context["request"].user != value:
            raise ValidationError("You can't create a post for another user.")
        return value

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep["author"] = UserSerializer(author).data

        return rep

    class Meta:
        model = Post
        # List of all the fields that can be included in a
        # request or a response
        fields = ["id", "author", "body", "edited", "created", "updated"]
        read_only_fields = ["edited"]

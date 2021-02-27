from rest_framework import serializers
from .models import Comment
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.HyperlinkedRelatedField(
    #     view_name = "UserDetail",
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = User
        fields = (
            "id",
            "ussername",
            "first_name",
            "last_name",
        )

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comment  = serializers.HyperlinkedRelatedField(
        view_name = "comment_detail",
        many=True,
        read_only=True
    )

    class Meta:
        model = Comment
        fields = (
            "id",
            "comment",
            "User"
        )
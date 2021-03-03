from rest_framework import serializers
from .models import Comment
from .models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = User
        fields = (
            "id",
            "ussername",
            "first_name",
            "last_name",
            "password"
        )

class CommentSerializer(serializers.ModelSerializer):
    #     Comment = serializers.HyperlinkedRelatedField(
    #     view_name="comment_detail",
    #     many=True,
    #     read_only=True
    # )

    class Meta:
        model = Comment
        user = UserSerializer()
        fields = (
            "id",
            "user",
            "comment",
            "likes"
        )
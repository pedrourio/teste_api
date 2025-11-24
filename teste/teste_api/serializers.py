from django.contrib.auth.models import User
from rest_framework import serializers
from teste.teste_api.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="post-detail"
    )
    
    class Meta:
        model = User
        fields = ["url", "username", "email", "password", "posts"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Post
        fields = ["url", "id", "title", "description", "created", "last_edit", "owner"]
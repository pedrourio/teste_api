from django.contrib.auth.models import User
from rest_framework import serializers
from teste.teste_api.models import Post


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Post.objects.all()
    )
    
    class Meta:
        model = User
        fields = ["url", "username", "email", "password", "posts"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    class Meta:
        model = Post
        fields = ["url", "title", "description", "created", "last_edit", "owner"]
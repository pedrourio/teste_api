from django.contrib.auth.models import  User
from teste.teste_api.models import Post
from rest_framework import permissions, viewsets
from teste.teste_api.permissions import IsOwnerOrAdminOrReadOnly


from teste.teste_api.serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("created")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

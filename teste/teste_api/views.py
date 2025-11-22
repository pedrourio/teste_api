from django.contrib.auth.models import  User
from teste.teste_api.models import Post
from rest_framework import permissions, viewsets
from teste.teste_api.permissions import IsOwnerOrAdminOrReadOnly


from teste.teste_api.serializers import UserSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        
        if self.action == 'destroy' or self.action == 'list' :
            return [permissions.IsAdminUser()]
        
        if self.action == 'update' or self.action == 'partial_update':
            return [IsOwnerOrAdminOrReadOnly()]
        


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("created")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

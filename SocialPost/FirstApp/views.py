from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Post
from .permissions import AuthorOrReadOnly,AuthorAdminOrReadOnly
from .serializers import PostSerializer
from django.db.models import Q

# by using below class we can return all public posts and private post of authenticated user.
class ListPost(generics.ListAPIView):
    permission_classes = [AllowAny]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            return Post.objects.all()
        elif current_user.is_authenticated:
            return Post.objects.filter(Q(user=current_user) | Q(is_private=False))
        return Post.objects.filter(is_private = False)

# user can post their own post by using below class
class ListUserPosts(generics.CreateAPIView):
    permission_classes = [AuthorOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_authenticated:
            return Post.objects.filter(Q(user=current_user) | Q(is_private=False))
        return Post.objects.filter(is_private = False)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# user can update thier own post by using below class
class UpdateUserPosts(generics.RetrieveUpdateAPIView):
    permission_classes = [AuthorOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_authenticated:
            return Post.objects.filter(Q(user=current_user))

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# delete the post by individual user or admin 
class DeleteUserPosts(generics.DestroyAPIView):
    permission_classes = [AuthorAdminOrReadOnly]
    authentication_classes = [JWTAuthentication]
    serializer_class = PostSerializer

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_superuser:
            print("True")
            return Post.objects.all()
        elif current_user.is_authenticated:
            return Post.objects.filter(Q(user=current_user))


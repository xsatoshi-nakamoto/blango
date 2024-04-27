from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers, vary_on_cookie
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from blog.models import Post, Tag, User
from .serializers import PostSerializer, TagSerializer
from rest_framework import  permissions
from django.db.models import Q
from django.utils import timezone

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [permissions.IsAuthenticated]

    @method_decorator(cache_page(300))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    @action(methods=["get"], detail=False, name="Posts by the logged in user")
    def mine(self, request):
        if request.user.is_anonymous:
            raise PermissionDenied("You must be logged in to see which Posts are yours")
        posts = self.get_queryset().filter(author=request.user)
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @method_decorator(cache_page(120))
    @method_decorator(vary_on_headers("Authorization", "Cookie"))
    def list(self, *args, **kwargs):
        return super(PostViewSet, self).list(*args, **kwargs)
        
    def get_queryset(self):
        if self.request.user.is_anonymous:
            # published only
            return self.queryset.filter(published_at__lte=timezone.now())

        if self.request.user.is_staff:
            # allow all
            return self.queryset

        # filter for own or
        return self.queryset.filter(
            Q(published_at__lte=timezone.now()) | Q(author=self.request.user)
        )

# class UserDetail(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     # serializer_class = UserSerializer
#     @method_decorator(cache_page(300))
#     def get(self, *args, **kwargs):
#         return super(UserDetail, self).get(*args, *kwargs)

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    @method_decorator(cache_page(300))
    def list(self, *args, **kwargs):
        return super(TagViewSet, self).list(*args, **kwargs)

    @method_decorator(cache_page(300))
    def retrieve(self, *args, **kwargs):
        return super(TagViewSet, self).retrieve(*args, **kwargs)
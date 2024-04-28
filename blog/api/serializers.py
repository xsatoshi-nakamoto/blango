from rest_framework import serializers
from blog.models import * 
from versatileimagefield.serializers import VersatileImageFieldSerializer

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'value']

class ContentTypeField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return ContentType.objects.all()
class CommentSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)
    content_type = ContentTypeField()
    content_object = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'creator', 'content', 'content_type', 'object_id', 'content_object', 'created_at', 'modified_at']

    def get_content_object(self, obj):
        return str(obj.content_object)

class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_at', 'modified_at', 'published_at', 'title', 'slug', 'summary', 'content', 'tags', 'comments']

class PostDetailSerializer(PostSerializer):
    author = serializers.PrimaryKeyRelatedField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'created_at', 'modified_at', 'published_at', 'title', 'slug', 'summary', 'content', 'tags', 'comments']
    hero_image = VersatileImageFieldSerializer(
        sizes=[
            ("full_size", "url"),
            ("thumbnail", "thumbnail__100x100"),
            ("square_crop", "crop__200x200"),
        ],
        read_only=True,
    )
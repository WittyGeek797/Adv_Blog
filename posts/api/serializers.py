from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField
)

from posts.models import Post

from comments.api.serializers import CommentSerializer, CommentDetailSerializer
from comments.models import Comment
from accounts.api.serializers import UserDetailSerializer

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
        ]

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            'url',
            'user',
            'title',
            'content',
            'publish',
        ]


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserDetailSerializer(read_only=True)
    image = SerializerMethodField()
    html = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'url',
            'id',
            'user',
            'title',
            'slug',
            'content',
            'html',
            'publish',
            'image',
            'comments',
        ]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None

        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

"""
data = {
		"title": "Testing Serializer",
		"slug": "got-a-swag",
		"content": "Lets see what happens",
		"publish": "2016-06-07",
}
	
obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj,data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item)
"""

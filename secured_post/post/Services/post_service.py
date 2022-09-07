
from post.serializers import PostSerializer

def create_post(create_data):
    post_serializer = PostSerializer(data = create_data)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()
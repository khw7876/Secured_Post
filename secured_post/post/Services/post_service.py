from post.models import Post as PostModel
from post.serializers import CreatePostSerializer, PostSerializer

def create_post(create_data):
    post_serializer = CreatePostSerializer(data = create_data)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

def update_post(update_data, post_id):
    update_post = PostModel.objects.get(id=post_id)
    post_serializer = PostSerializer(update_post, update_data, partial= True)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

def check_password(check_data, post_id):
    check_post = PostModel.objects.get(id=post_id)
    if check_data["password"] == check_post.password:
        return True
    return False
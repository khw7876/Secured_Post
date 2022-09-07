from django.contrib.auth.hashers import check_password

from post.models import Post as PostModel
from post.serializers import CreatePostSerializer, PostSerializer

def create_post(create_data):
    post_serializer = CreatePostSerializer(data = create_data)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

def update_post(update_data, post_id):
    update_post_obj = PostModel.objects.get(id=post_id)
    post_serializer = PostSerializer(update_post_obj, update_data, partial= True)
    post_serializer.is_valid(raise_exception=True)
    post_serializer.save()

def check_is_password(check_data, post_id):
    check_post = PostModel.objects.get(id=post_id)
    if check_password(check_data["password"], check_post.password):
        return True
    return False

def delete_post(post_id):
    delete_post_obj = PostModel.objects.get(id=post_id)
    delete_post_obj.delete()
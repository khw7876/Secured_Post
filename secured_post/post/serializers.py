from rest_framework import serializers

from post.models import Post as PostModel


class PostSerializer(serializers.ModelSerializer):
    def validate(self, data):
        condition = all(x not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"] for x in data["password"])
        if len(data["password"]) < 6 or condition
            raise serializers.ValidationError("비밀번호는 6자 이상, 숫자를 꼭 포함해주세요!")
        return data
    
    def create(self, *args, **kwargs):
        post = super().create(*args, **kwargs)
        p = post.password
        post.set_password(p)
        post.save()
        return post

    class Meta:
        model = PostModel
        fields = "__all__"
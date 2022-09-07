from rest_framework.views import APIView
from rest_framework import status, exceptions
from rest_framework.response import Response

from post.Services.post_service import create_post

# Create your views here.

class PostView(APIView):

    def post(self, request):
        create_post(request.data)
        return Response({"detail" : "게시글을 작성하였습니다."}, status=status.HTTP_200_OK)
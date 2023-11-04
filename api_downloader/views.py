from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .utils import *

class PopularVideos(APIView):
    def get(self, request):
        response = get_popular_videos()
        return Response(data=response, status=status.HTTP_200_OK)
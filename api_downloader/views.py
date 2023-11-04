from urllib import response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .utils import *


class PopularVideos(APIView):
    def get(self, request):
        response = get_popular_videos()
        return Response(data=response, status=status.HTTP_200_OK)


class SearchVideos(APIView):
    def get(self, request):
        search_keys = request.GET.get("search_keys")
        page_token = request.GET.get("page_token")

        if page_token:
            response = search_pagination(search_keys, page_token)
        else:
            response = search_video(search_keys)
        return Response(data=response, status=status.HTTP_200_OK)


class SearchPaginated(APIView):
    def get(self, request, search_keys, page_token):
        response = search_pagination(search_keys, page_token)
        return Response(data=response, status=status.HTTP_200_OK)

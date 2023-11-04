from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import StreamingHttpResponse
from .utils import *
import threading



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


class GetSingleVideo(APIView):
    def get(self, request, video_id):
        response = get_single_video(video_id)
        return Response(data=response, status=status.HTTP_200_OK)


class GetSingleChannel(APIView):
    def get(self, request, channel_id):
        response = get_channel_info(channel_id)
        return Response(data=response, status=status.HTTP_200_OK)

class DownloadVideo(APIView):
    def get(self, request, video_id):
        download_thread = threading.Thread(target=download_video, args=(video_id,))
        download_thread.start()
        return Response({"message": "Download started"}, status=status.HTTP_200_OK)
    

# class DownloadVideo(APIView):
#     def get(self, request, video_id):
#         video_stream = download_video(video_id)

#         if video_stream.startswith("Error"):
#             return Response({"message": video_stream}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#         response = StreamingHttpResponse(video_stream, content_type="video/mp4")
#         response['Content-Disposition'] = f'attachment; filename="{video_id}.mp4"'
#         return response
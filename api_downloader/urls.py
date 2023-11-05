from django.urls import path
from .views import *

app_name = "api_downloader"

urlpatterns = [
    path("popular/", PopularVideos.as_view(), name="most_popular"),
    path("search/", SearchVideos.as_view(), name="search_video"),
    path("video/details/<str:video_id>/", GetSingleVideo.as_view(), name="video_details"),
    path("channel/details/<str:channel_id>/", GetSingleChannel.as_view(), name="channel_details"),
    path("download/<str:video_id>/", DownloadVideo.as_view(), name="download_video"),
]
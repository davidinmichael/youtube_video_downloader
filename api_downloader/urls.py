from django.urls import path
from .views import *


urlpatterns = [
    path("popular/", PopularVideos.as_view()),
    path("search/", SearchVideos.as_view()),
    path("video/details/<str:video_id>/", GetSingleVideo.as_view()),
    path("channel/details/<str:channel_id>/", GetSingleChannel.as_view()),
    path("download/<str:video_id>/", DownloadVideo.as_view()),
]
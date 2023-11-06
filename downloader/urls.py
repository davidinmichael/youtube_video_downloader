from django.urls import path
from .views import *

app_name = "downloader"

urlpatterns = [
    path("", index, name="home"),
    path("video_details/", get_video, name="get_video"),
    path("search/", search_videos, name="search_video"),
    path("download/", download_videos, name="download"),
]

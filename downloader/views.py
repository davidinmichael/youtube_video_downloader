from multiprocessing import context
from django.shortcuts import render
import requests

def index(request):
    url = "http://127.0.0.1:8000/api/popular"
    response = requests.get(url).json()
    context = {
        "items": response["items"],
        "head": "Most Popular Videos"
    }
    return render(request, "downloader/index.html", context)


def get_video(request):
    video_id = request.GET.get("video_id")
    url = f"http://127.0.0.1:8000/api/video/details/{video_id}"
    response = requests.get(url).json()
    context = {
        "items": response["items"]
    }
    return render(request, "downloader/get-video.html", context)